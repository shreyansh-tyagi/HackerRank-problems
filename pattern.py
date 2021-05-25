'''
Print the corresponding pattern for different values of ‘n’

Input Format

Enter the value of ‘n’.

Constraints

1<= n <= 10

Output Format

Print the required pattern

Sample Input 0

3
Sample Output 0

***
**
*

'''
n=int(input())
a=n
for i in range(n):
    for j in range(a):
        print('*',end='')
    a-=1    
    print()    