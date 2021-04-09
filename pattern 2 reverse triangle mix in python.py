'''Ravi wants to propose Anjali but Anjali loves Half PATTERNS. Anjali will only accept the proposal if Ravi gifts the best PATTERN to her. Ravi bought the 'Heart of the Ocean' the most expensive HALF diamond for Anjali but now he need Rs 55 to buy a diamond shaped gift wrapper.As his friend you have to help Ravi by building a diamond shaped gift wrapper so he can print it out, wrap it up and gift it to Anjali.

Input Format

Input contains only one thing n.

Constraints

n<=10

Output Format

Obtain that PATTERN

Sample Input 0

3
Sample Output 0

******
**  **
*    *

'''

n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    for k in range(i):
        print('  ',end='')
    for l in range(n-i):
        print('*',end='')
    print()    
    