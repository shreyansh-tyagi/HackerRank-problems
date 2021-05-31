'''

Given two different sets ‘A’ & ‘B’ of Integers with ‘n’ & ‘m’ elements respectively. Find the number of one-one functions possible.

Input Format

Enter the value of ‘n’ & ‘m’ separated by space.

Constraints

1 <= n,m <=10

Output Format

Print the output.
5 4
Sample Output 0

120
Sample Input 1

5 3
Sample Output 1

60

'''

from itertools import permutations 
b,c=map(int,input().split())
a=(list(permutations(range(b), c))) 
print(len(a))
