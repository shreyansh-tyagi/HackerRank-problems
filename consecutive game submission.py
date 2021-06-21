'''
Determines whether elements in an array can be re-arranged to form a consecutive list of numbers where each number appears exactly once.

[5, 1, 4, 3, 2] ➞ true

[5, 1, 4, 3, 2, 8]) ➞ false

Input Format

first line consists single integer N(length of array) second line consists N-separated values of array.

Constraints

0<=N<=100

Output Format

output should be 1 for true otherwise 0.

Sample Input 0

5
5 1 4 3 2
Sample Output 0

1
Sample Input 1

6
5 1 4 3 2 8
Sample Output 1

0
'''

n=int(input())
l=list(map(int,input().split()))[:n]
l.sort()
a=l[1]-l[0]
for i in range(len(l)-1):
    if l[i+1]-l[i]==a:
        b='1'
    else:
        b='0'
if b=='1':
    print('1')
else:
    print('0')