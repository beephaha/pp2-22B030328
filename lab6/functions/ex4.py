import math as mtn
import time as tm

def sqrtWithDelay(num, time):
    tm.sleep(time/1000)
    return mtn.sqrt(num)

num = int(input())
time = int(input())
print(sqrtWithDelay(num, time))