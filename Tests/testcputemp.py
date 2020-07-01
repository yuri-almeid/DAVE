#!/usr/bin/env python
import os

def get_temp():
    res = os.popen('vcgencmd measure_temp').readline()
    CPU = res.replace("temp=", '').replace("'C\n",'')
    CPU = str(CPU)
    return(CPU)


print (get_temp())

