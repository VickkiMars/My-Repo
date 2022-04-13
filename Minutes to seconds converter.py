# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:12:05 2022

@author: Victor
"""

#minute to seconds converter
def convert_minutes_to_seconds():
    
    take_input_hours = int(input("(IF THERE ISN'T ANY, ENTER '0') Time in hours >>> "))
    take_input_minutes = int(input('Time in minutes >>> '))
    
    tim = str(take_input_minutes)
    tih = str(take_input_hours)
    
    #mts = minutes to seconds
    htm = (take_input_hours*60)
    mts_for_hours = (htm*60)
    mts_for_minutes = (take_input_minutes*60)
    
    #a is the result gotten from converting input entered in hours to minutes
    a = htm + take_input_minutes
    A = str(a)
    
    
    #MTS - total minutes to seconds
    MTS = mts_for_hours + mts_for_minutes
    
    s = str(MTS)
    x = 'There are ' + s + ' seconds in ' + tim + ' Minute(s)' 
    y = 'There are ' + s + ' seconds in ' + tih + ' Hour(s)'
    
    #elif should have been used here but for its complexity
    #this code is written with a novice in mind
    
    if (tih != '0') and (tim == '0'):
        print(y)
    else:
        pass
    
    if ((tih != '0') and (tim != '0')):
        print('There are ' + s + ' seconds in ' + A + ' minutes' )
    else:
        pass
    
    if ((tih == '0') and (tim != '0')):
        print(x)
    else:
        pass

    
    
convert_minutes_to_seconds()