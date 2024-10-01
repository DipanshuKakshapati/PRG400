import time
from example_python import sum_loop as python_sum_loop
from example import sum_loop as cython_sum_loop

n = 10**6

start = time.time()
python_sum_loop(n)
print(f"Python version took: {time.time() - start:.5f} seconds")

start = time.time()
cython_sum_loop(n)
print(f"Cython version took: {time.time() - start:.5f} seconds")