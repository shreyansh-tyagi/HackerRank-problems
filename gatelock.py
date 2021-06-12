'''

Arjun is working in a very big IT professional company. This company is popular for maintaining and keeping its user’s data secure and consistent. For this purpose, the company has a separate secret room for storing all its data. Arjun has to go into this room for some work. But it has some secret lock on the entrance gate.
The lock consists of two buttons: a red button and a green button and a display showing some positive integer. After clicking the red button, the device multiplies the given number by two. After clicking the green button, the device subtracts one from the number on display. If at some point, the number stops being positive, it breaks down.  The device can show arbitrarily large numbers. Initially, the lock is showing any arbitrary number n.
Arjun wants to get the number m on display to open the lock. What is the minimum number of clicks he has to make to open the lock?

 

## Input Format

The first and only line of input contains two distinct integers n and m.

 

## Output Format

Print a single number- The minimum number of times one needs to push the button required to get the number m out of number n.

 

## Constraints


'''
import math
n,m=map(int,input().split())
count=0
while(m>n):
    if(m%2==0):
        m=m/2
        count+=1
    else:
        m+=1
        count+=1
print(math.trunc(count+n-m))