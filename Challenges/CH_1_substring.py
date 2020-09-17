#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 17:55:29 2020

@author: nikhildhamne
"""
"""
String Challenge
Have the function StringChallenge(str) take the str parameter 
being passed which will contain the numbers 2 through 9, and 
determine if there is a consecutive stream of digits of at least 
N length where N is the actual digit value. If so, return the 
string true, otherwise return the string false. For example: 
if str is "6539923335" then your program should return the 
string true because there is a consecutive stream of 3's of 
length 3. The input string will always contain at least one digit. 
Examples
Input: "5556293383563665" 
Output: false
Input: "5788888888882339999" 
Output: true
"""


def StringChallenge(strParam):
  # code goes here
  # Checking validity of input
  # First check if input is numbers
  if len(strParam)==0 or not(strParam.isdigit()):
    print("Invalid Input")
    return strParam
  # THen check if numbers are between 2-9
  if ('1' or '0') in strParam:
    print("Contains invalid digits")
    return strParam
  # create a list of substrings that is to be serached for
  matches = []
  for i in range(2,10):
    matches.append(str(i)*i)
  # finding substring
  if any(x in strParam for x in matches):
    print("True")
  else:
    print("False")
  return strParam

# keep this function call here 
data = input()
print(StringChallenge(data))