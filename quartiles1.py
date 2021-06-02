'''
Objective
In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given an array, , of  integers, calculate the respective first quartile (), second quartile (), and third quartile (). It is guaranteed that , , and  are integers.

Example

The sorted array is  which has an odd number of elements. The lower half consists of , and its median is . The middle element is  and represents the second quartile. The upper half is  and its median is . Return .


The array is already sorted. The lower half is  with a median = . The median of the entire array is , and of the upper half is . Return .

Function Description

Complete the quartiles function in the editor below.

quartiles has the following parameters:

int arr[n]: the values to segregate
Returns

int[3]: the medians of the left half of ,  in total, and the right half of .
Input Format

The first line contains an integer, , the number of elements in .
The second line contains  space-separated integers, each an .

Constraints

, where  is the  element of the array.
Sample Input

STDIN                   Function
-----                   --------    
9                       arr[] size n = 9 
3 7 8 5 12 14 21 13 18  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
Sample Output

6
12
16
Explanation

. There is an odd number of elements, and the middle element, the median, is .

As there are an odd number of data points, we do not include the median (the central value in the ordered list) in either half:

Lower half (L): 3, 5, 7, 8

Upper half (U): 13, 14, 18, 21

Now find the quartiles:

 is the . So, .
 is the . So, .
 is the . So, .

'''

import statistics
import math
n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
b,c,e=[],[],[]
if(n%2!=0):
    b.append(a[(n-1)//2])
    d=(n-1)//2
    for i in range(d):
        c.append(a[i])
    for i in range(d+1,n):
        e.append(a[i])
    b.append(math.trunc(statistics.median(c)))
    b.append(math.trunc(statistics.median(e)))
    b.sort()
    for i in range(len(b)):
        print(b[i])
else:
    d=(n-2)//2
    for i in range(d+1):
        c.append(a[i])
    for i in range(d+1,n):
        e.append(a[i])
   
    b.append(math.trunc(statistics.median(c)))
    b.append(math.trunc(statistics.median(e)))
    b.append(math.trunc(statistics.median(a)))
           
    b.sort()
    for i in range(len(b)):
        print(b[i])    
                                    