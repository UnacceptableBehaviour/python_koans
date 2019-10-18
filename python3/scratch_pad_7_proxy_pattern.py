#!/usr/bin/env python

# from: https://stackoverflow.com/questions/23937189/how-do-i-use-subprocesses-to-force-python-to-release-memory/24126616#24126616
# converted to 3.7

import multiprocessing, random, sys, os, time
from pprint import pprint

# utility function for clarity - runs in subprocess
def create_list(size):
    # https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3
    #maxint = sys.maxint # 2.7 - 9223372036854775807
    maxint = sys.maxsize # 3.7 - 9223372036854775807    
    randrange = random.randrange # <bound method Random.randrange of <random.Random object at 0x7feffa83ec20>>
    print(f"SIZE passed in:{size}") # SIZE passed in:5000000
    
    # https://stackoverflow.com/questions/15014310/why-is-there-no-xrange-function-in-python3
    # interestin metrics tests ^
    return [randrange(maxint) for i in range(size)] # 2.7 xrange renamed range in 3.7
    # range(5*1000*1000) = range(0, 5000000)
    # random.randrange(sys.maxsize) 
    # 4483828468040413747, 8493894937573293349, 908943212521800595 etc etc 5000000 list elements


def run_test(state):
    # this function is run in a separate process
    size = state['list_size']
    state['sub_process'] = os.getpid()
    print(f"creating a list with {size} random elements - this can take a while... ")
    sys.stdout.flush()
    lst = create_list(size)
    t0 = time.time()
    print('list created . . sorting', t0)    
    lst.sort()
    t1 = time.time()
    state['time'] = t1 - t0
    print('sorted', t1)    


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    state = manager.dict(list_size=5*1000*1000)  # shared state
    print("STATE:")                     # {'list_size' = 5000000}
    pprint(state)                       # <DictProxy object, typeid 'dict' at 0x10ca13dd0>
    print(state['list_size'])           # 5000000
    print(f"Dict size {len(state)} <"); # Dict size 1 <    
    pprint(run_test)                    # <function run_test at 0x10310d5f0>
    
    #
    #
    #####
    
    # multiprocess vs threading
    #  os.cpu_count()
    # https://youtu.be/ecKWiaHCEKs # concise demo TODO - demo
    # threding - lock acqruie/release alocation
    # https://www.youtube.com/watch?v=EKC_jcFH98o - from 40m
    #
    p = multiprocessing.Process(target=run_test, args=(state,)) # args ({'list_size' = 5000000}, ) < tuple!
    p.start()    # fire it up             ^
    p.join()     # wait for completion
    
    #####
    #
    #    
    
    print(f"time to sort: {round(state['time'],3)}")    
    print(f"subproces PID is {state['sub_process']}, sleeping for a minute...")
    print(f"my PID is {os.getpid()}, sleeping for a minute...")
    time.sleep(10)
    # at this point you can inspect the running process to see that it
    # does not consume excess memory
    
# (venv) python3 $ ./scratch_6_sub_p_mem.py 
# STATE:
# <DictProxy object, typeid 'dict' at 0x10d0d14d0>
# 5000000
# Dict size 1 <
# <function run_test at 0x10d0e05f0>
# creating a list with 5000000 random elements - this can take a while... 
# SIZE passed in:5000000
# list created . . sorting 1571077252.802976
# sorted 1571077257.3136902
# time to sort: 4.511
# subproces PID is 3298, sleeping for a minute...
# my PID is 3296, sleeping for a minute...


# PID   COMMAND      %CPU  TIME     #TH   #WQ  #PORT MEM    PURG   CMPR PGRP PPID STATE    BOOSTS         %CPU_ME %CPU_OTHRS UID  FAULTS   COW    MSGSENT   MSGRECV   SYSBSD
# 3298  Python       98.9  00:07.31 1/1   0    8     279M+  0B     0B   3296 3296 running  *0[1]          0.00000 0.00000    501  81581+   707+   58        29        1320+
# 3297  Python       0.0   00:00.01 4     0    11    4276K  0B     0B   3296 3296 sleeping *0[1]          0.00000 0.00000    501  1797     754    10        5         337+
# 3296  Python       0.0   00:00.08 1     0    13    7252K  0B     0B   3296 1723 sleeping *0[1]          0.00000 0.00000    501  3999     1180   116       54        1572


# TODO - implement process & thread comparison
# https://www.youtube.com/watch?v=ecKWiaHCEKs&feature=youtu.be

