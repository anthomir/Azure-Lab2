# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    filenames = ["mrinput-1.txt", "mrinput-2.txt", "mrinput-3.txt", "mrinput-4.txt"]
    input_data = yield context.call_activity("getinputdatafn", filenames)

    map_tasks = []
    for data in input_data:
        map_tasks.append(context.call_activity('Mapper', data))
    
    map_results = yield context.task_all(map_tasks)

    shuffler_tasks = []
    for result in map_results:
        shuffler_tasks.append(context.call_activity('Shuffler', result))

    shuffled_data = yield context.task_all(shuffler_tasks)

    reducer_tasks = []
    for data in shuffled_data:
        reducer_tasks.append(context.call_activity('Reducer', data))

    reduced_data = yield context.task_all(reducer_tasks)
    print(reduced_data)
    final_result = {}
    for word_list in reduced_data:
        for word_dict in word_list:
            word = word_dict['Word']
            count = word_dict['Count']
            if word in final_result:
                final_result[word] += count
            else:
                final_result[word] = count
    print(final_result)
    return final_result

main = df.Orchestrator.create(orchestrator_function)
