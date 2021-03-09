
# Citlaly Garcia 
# CSE 5408 Spring 2021 
# Lab 4: GitHub - Advanced 
# Part c: Time Conversion 
# Group: APP-itizer Enthusiasts 

import datetime 

def converttomilitary(str1):

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "AM": 
        return str1[:-2] 

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

now = datetime.datetime.now()
print ("Current time: ")
print (now.strftime("%I:%M:%S%p"))
str=now.strftime("%I:%M:%S%p")
print(converttomilitary(str))

print ("Current date and time: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

    