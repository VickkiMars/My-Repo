# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:51:17 2022

@author: Victor
"""

def convert_minutes_to_hours():
    take_input_minute  = int(input('Time in Minutes >>> '))
    tim = str(take_input_minute)
    
    mth = take_input_minute/60
    MTH = str(mth)
    
    output = 'There are (is) ' + MTH + ' Hour(s) in ' + tim + ' minute(s)'
    print(output)
    
convert_minutes_to_hours()