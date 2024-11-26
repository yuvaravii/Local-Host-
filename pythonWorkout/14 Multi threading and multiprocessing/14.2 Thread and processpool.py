from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(numbers):
    time.sleep(1)
    return f"Numbers : {numbers}"

def print_letters(letters):
    time.sleep(1.5)
    return f"Letters : {letters}"


# need iterable 
ls1 = [1,2,3,4,5,6,7,8,9]


startTime = time.time()
with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(print_numbers,ls1)


endTime = time.time()
timeTaken = endTime - startTime
print(f"Time taken : {timeTaken}")

for result in results:
    print(result)
