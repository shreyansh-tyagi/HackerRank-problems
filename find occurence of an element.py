'''
An array of size n, find all elements in array that appear more than n/k times. For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3.

Input Format

First line consists the size of an array. Second line consists the element of an array. Third line consists the value of k.

Constraints

1 < N <= 10^5 1 < Ai <=999

Output Format

Output contain the elements that appear more than n/k times.

Sample Input 0

8
5 4 3 5 6 5 1 5
4
Sample Output 0

5

'''
a=int(input())
b=list(map(int,input().split()))[:a]
c=int(input())
d=[]
for i in range(a):
    if b.count(i)>a//c:
        d.append(b[i])
d=list(set(d))        
for i in range(len(d)):
    print(d[i],end=' ')