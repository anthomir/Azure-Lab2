# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from azure.storage.blob import BlobServiceClient
from azure.identity import DefaultAzureCredential

def main(filenames):
    connect_str = "DefaultEndpointsProtocol=https;AccountName=mapreducerbb48;AccountKey=Ay9U0RuaQh2aVAl+w8E5pggENSHkw77ezDWQPnDoD0uyMLRLkoVX8f/1ogsP7EMhAo+8LBBBqFjr+AStFPcv8Q==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client("scm-releases")

    input_data = []
    for filename in filenames:
        blob_client = container_client.get_blob_client(filename)
        blob_content = blob_client.download_blob().readall().decode("utf-8")
        
        lines = blob_content.split('\n')
        for index, line in enumerate(lines):
            input_data.append((index, line)) 
    
    return input_data

