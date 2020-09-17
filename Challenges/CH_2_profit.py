#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 18:02:28 2020

@author: nikhildhamne
"""
"""
Array Challenge
Have the function ArrayChallenge(arr) take the array 
of numbers stored in arr which will contain integers 
that represent the amount in dollars that a single 
stock is worth, and return the maximum profit that 
could have been made by buying stock on day x and 
selling stock on day y where y > x. For example: if 
arr is [44, 30, 24, 32, 35, 30, 40, 38, 15] then 
your program should return 16 because at index 2 
the stock was worth $24 and at index 6 the stock 
was then worth $40, so if you bought the stock at 
24 and sold it at 40, you would have made a profit 
of $16, which is the maximum profit that could have 
been made with this list of stock prices. 

If there is not profit that could have been made with the stock prices, then your program should return -1. For example: arr is [10, 9, 8, 2] then your program should return -1. 
Examples
Input: [10,12,4,5,9] 
Output: 5
Input: [14,20,4,12,5,11] 
Output: 8
"""

#import numpy as np 
def ArrayChallenge(arr):
  # code goes here
  # make a copy of array so that the original data remains untouched
  arr1=arr
  # make a profit array
  profit_arr=[]

  for i in range(len(arr1)):
    for j in range(0,len(arr1)):
      profit = arr1[j]-arr[i]
      profit_arr.append(profit)
    arr1=arr1[1:len(arr1)]
  print(max(profit_arr))
  return arr

# keep this function call here 
arr = [14,20,4,12,5,11] 
print(ArrayChallenge(arr))