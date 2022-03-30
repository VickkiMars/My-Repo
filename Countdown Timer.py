# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:39:56 2022

@author: Victor
"""

import time
  
# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
#the divmod() method takes two numbers and returns a pair of numbers(a tuple) consisting of their quotient and remainder
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    print(' Your countdown is over!!')
  
  
# input time in seconds
t = input("Enter the time in seconds: ")
  
# function call
countdown(int(t))
 
