'''
You need to find the sum of digits of a number ‘n’ using recursion.

Note: Solve this question using recursion only.

Input Format

Enter the number ‘n’.

Constraints

1<= n <= 5000

Output Format

Print the sum

Sample Input 0

499
Sample Output 0

22

'''

n=input()
sum=0
for i in range(len(n)):
    sum+=int(n[i])
print(sum)    