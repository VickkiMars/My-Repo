# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 23:25:21 2022

@author: Victor
"""

#tip calculator
#a sum of money customarily given by a customer to certain service sector workers for the service they have performed, in addition to the basic price of the service. anticipated

print("Currency symbols")
print("1.   ₦ = Naira")
print("2.   $ = Dollar")
print("3.   € = Euro")
print("4.   £ = Pound")
print("::::::::::::::::::::::::::::::::::::::::::")
print("")


currency_select = input("Please Input Your currency Name {exactly as shown above!!}: ")

#this is the actual money paid for the service
bill = float(input("Bill Paid "+ "(" + currency_select + ") : "))

#this is the percentage given as tip(8%)
tip = 0.08

#this is the number of people you are giving the tip to
nop = float(input("Number of People: "))


Tip_per_person = (bill*tip)/nop
Total_per_person = (bill+Tip_per_person)

tipp = str(Tip_per_person)
Tpp = str(Total_per_person)
Tipp = int(Tip_per_person)

print("Tip per person: " + tipp + "(" + currency_select + ")")
print("Total_per_person: " + Tpp + "(" + currency_select + ")")

if Tipp < 5:
    print("The tip is too small, either you pay a higher amount or you don't pay at all")
else:
    pass