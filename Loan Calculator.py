"""
Created on Thu Mar  3 22:10:52 2022

@author: Victor
"""

#loan calculator

loan_amount = str(input("Loan Amount (Naira) : "))
la = int(loan_amount)

loan_term = str(input("Loan Duration  (Months) : "))
lt = int(loan_term)

interest_rate = 6

interest = (la * lt*interest_rate)/100
i = str(interest)

final_amount = interest + la
fa = str(final_amount)

print("Amount to be paid back is: " + fa)
print("Interest added is: " + i)
