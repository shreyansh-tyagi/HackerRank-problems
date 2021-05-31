'''
In a round table conference the comissioner decided to meet with ‘n’ junior fellows. All the fellows along with commisioner will sit around a table. In how many ways they can sit around the table.

Input Format

Enter the value of ‘n’

Constraints

5 <= n <=10

Output Format

Print the output.

Sample Input 0

6
Sample Output 0

60
'''
import math
n=int(input())
p=n
a=n
while n>3:
    p=p*(n-1)
    n=n-1
print(math.trunc(p/a))