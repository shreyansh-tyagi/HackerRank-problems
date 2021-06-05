'''
Solve the following series by observing the reuired patterns.

1 + 2 + 3 + 4 + 5 + 6 = 90

2 + 6 + 9 + 5 + 8 + 1 = 238

9 + 4 + 2 + 3 + 5 + 7 = ?

Input Format

Input contain of 6 numbers.

Constraints

No more constraints

Output Format

Print the desired output

Sample Input 0

1 2 3 4 5 6
Sample Output 0

90
Sample Input 1

2 6 9 5 8 1
Sample Output 1

238
'''

a=list(map(int,input().split()))[:6]
b,c=sum(a[0:3]),sum(a[3:])
print(b*c)
    