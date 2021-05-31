'''
In operating system we have ‘n’ process to schedule and each process require min ‘k’ resources for complete execution. Find out the minimum number of resources that CPU should have to schedule all the process without deadlock.

Input Format

Enter the value of n & k respectively

Constraints

1 <= n,k <= 10

Output Format

Print the required resources

Sample Input 0

3 4
Sample Output 0

10
Sample Input 1

5 4
Sample Output 1

16
'''
p,n=map(int,input().split())
r=p*(n-1)+1
print(r)