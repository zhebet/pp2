import time
import math

def square_root_after_milliseconds(n, m):
    time.sleep(m / 1000)
    sqrt = math.sqrt(n)
    return sqrt

n = int(input())
m = int(input())

r = square_root_after_milliseconds(n, m)

print(r)