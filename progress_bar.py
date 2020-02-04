import sys
import time
import math
import random

# 全部で20個ということにする
# 5%で1個


def get_progress_bar(cur, entire):
    raw_ratio = cur/entire*100
    ratio = math.floor(raw_ratio)
    progress = ratio//5;
    ret = "["
    for i in range(progress-1):
        ret += "="
    ret += ">"
    for i in range(20-progress):
        ret += " "
    ret += "]  "
    out_per = math.floor(raw_ratio*100)/100
    if out_per > 100:
        out_per = 100.0
    ret += str(out_per)+"%"
    return ret

def pretend_sleep(x):
    start = time.time()
    while (True):
        spend = time.time()
        cur = (spend-start)
        time.sleep(random.uniform(0.01, 0.2))
        sys.stderr.write("\r\033[K"+ get_progress_bar(cur,x))
        sys.stderr.flush()
        if spend-start >= x:
            break

    print("\r[====================] \033[1;32m DONE!!  ")


x = input()
pretend_sleep(float(x))
