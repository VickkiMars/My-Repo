# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:20:41 2022

@author: Victor
"""

#miles to kilometers converter
def convert_miles_to_kilometers():
    mile = input("Mile(s) >>> ")
    Mile = str(mile)
    MIle = float(mile)

    kilometers = MIle*1.61
    Kilometers = str(kilometers)
    
    output = "There are " + Kilometers + " Kilometers in " + Mile + " Mile(s)"
    
    print(output)
    
convert_miles_to_kilometers()
