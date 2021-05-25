'''
Verify the series and print the output.

1 + 2 + 3 + 4 + 5 + 6 = 9

2 + 6 + 9 + 5 + 8 + 1 = 15

9 + 4 + 2 + 3 + 5 + 7 = ?

Input Format

Enter 6 different elements

Constraints

Number can lie between (1,20).

Output Format

Print the desired sum.

Sample Input 0

1 2 3 4 5 6
Sample Output 0

9
'''
a=list(map(int,input().split()))[:6]
sum=0
for i in range(len(a)):
    if(a[i]%2!=0):
        sum+=a[i]
print(sum)        