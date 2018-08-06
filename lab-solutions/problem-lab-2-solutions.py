#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solutions for the first problem set at the Exploring Economics Summer School 2018

@author: Claudius Graebner
@email: claudius@claudius-graebner.com

Note: There are many more solutions to the tasks, and often there is not really
the 'best' way to do it.

"""

#%% Task 1
# The task was to identify errors in code chunks.

#%% 1.0.
"""Sum integers from 1 to 10"""

result = 0
for i in range(10): # Colon was missing
    result += i

#%% 1.1.
"""Sum integers from 1 to 10"""
result = 0 
i = 1
while i <= 10: # Colon was missing
    result += i

#%% 1.2.
"""Function to compute relation of two arguments a and b"""
def rel(a, b): 
    return a / b
a = 2 # This must be a float or an integer, not a string
b = 20
result = rel(a, b)

#%% 1.3. - 1.5.
"""Function to compute factorial of integer b"""
def factorial(result , a): 
    if a > 1:
        result = factorial(result , a-1) 
    result *= a
    return result # Result statement was missing

b = 5
result = factorial(1, b) # Argument 1 was missing
print(result)

#%% Task 2

# Write a python script to compute the sum of all integer numbers between 0 and 100 
# that are not evenly (without remainder) divisible by either 4 or 5. 
# That is, the numbers {1, 2, 3, 6, 7, 9, 11, 13, 14, 17, 18, ...}

x = range(101)
y = []

for i in range(100):
    if (i%4>0) & (i%5>0):
        y.append(i)
sum(y)

#%% Task 3

# Consider the code in problem 2 again and rewrite the computation as a function
# such that the intervals (from 0 to 100 in problem 2) can be passed as arguments. 
# Use this function to compute the sums of all integers not divisible by 4 or 5 
# in the following intervals [100,300], [100,300], [10000, 20000].

def sol_func(p):
    y=[]
    for i in p:
        if (i%4>0) & (i%5>0):
            y.append(i)
    print(y)
    sum_y = sum(y)
    return(sum_y)

sol_func(range(100, 301))
sol_func(range(10000, 20001))

#%% Task 4

# Write a python function to compute the n’th Fibonacci number. 
# E.g, the function called with argument 9 should return 34; with argument 10, 
# it should return 55 etc.

def fib_func(x):
    k = 0
    fib_seq = [1, 1]
    while k < x-2:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
        k += 1
    return(fib_seq[-1])

#%% Task 5
    
# Use the function from problem 4 to compute the 40th Fibonacci number.
    
fib_func(40)
