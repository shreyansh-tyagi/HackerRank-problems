/**Given an array of integers, find the sum of its elements.

For example, if the array ar=[1,2,-8,1,5], so 1+5 return 6.

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers

Input Format

The first line contains an integer, n, denoting the size of the array. The second line contains n space-separated integers representing the array's elements.

Constraints

0

Output Format

Print the sum of the array's elements as a single integer.

Sample Input 0

6
1 2 3 4 10 11
Sample Output 0

14  **/

import array as arr
n=int(input())
a=list(map(int,input().split()))[:n]
b=arr.array('i',a)
sum=0
for i in range(0,len(b),2):
     if b[i]>0:
            sum+=b[i]
print(sum)