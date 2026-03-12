#!/usr/bin/env python

from time import sleep
'''

    Print function with flush parameter
    Created by : Andris Mežals
    URL:
    https://www.includehelp.com/python/flush-parameters-in-python-with-print-function.aspx
    

'''
# output is flushed now
print('es mācos programmēt ', end='', flush=True)
sleep(1)
print('lietoju funkciju print ', end='', flush=True)
sleep(1)
print('ar parametru flush. ', end='', flush=True)
sleep(1)

sleep(5)
print('Bye! <(0v0)>') 
input('Press <ENTER> to exit.')
