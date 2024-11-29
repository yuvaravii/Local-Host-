import sys
import multiprocessing
import os
import math
import time

## creating a function that performs a multi-processing.
# set a sys requirement more than the default one
sys.set_int_max_str_digits(100000)

# function
def get_factorial(number):
    print(f"Computing the factorial of {number}")
    result = math.factorial(number)
    print(f"The factorial of {number} is : {result}")
    return result


if __name__ == "__main__":
    numbers = [6000,7000,8000]
    startTime = time.time()
 
    with multiprocessing.Pool() as pool:
        results = pool.map(get_factorial,numbers)

    endTime = time.time()
    totalTimeTaken = endTime - startTime

    print(f"Results : {results}")
    print(f"Time taken for execution : {totalTimeTaken} seconds")