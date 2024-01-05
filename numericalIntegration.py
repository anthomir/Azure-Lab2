import math

def numerical_integration(lower, upper, N):
    delta_x = (upper - lower) / N
    result = 0.0

    for i in range(N):
        x_i = lower + i * delta_x
        result += abs(math.sin(x_i)) * delta_x

    return result

def main():
    interval_lower = 0
    interval_upper = 3.14159
    iterations = [10, 100, 100, 1000, 10000, 100000, 1000000]

    for N in iterations:
        integral_result = numerical_integration(interval_lower, interval_upper, N)
        print(f"N = {N}: {integral_result}")


main()