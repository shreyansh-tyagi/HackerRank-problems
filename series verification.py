'''

1,2,4,8,16...... for(n=2)

1,3,9,27,81,..... for(n=3)

1,4,16,64,256,.... for (n=4)

Print the eighth term of the series.

Input Format

Enter the value of ‘n’.

Constraints

1 <= n <= 8

Output Format

Print the eighth term.

Sample Input 0

2
Sample Output 0

128

'''

n=int(input())
a=[1]
b=1
for i in range(8):
    b=b*n
    a.append(b)
print(a[7])    
    
