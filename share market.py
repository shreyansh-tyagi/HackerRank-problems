'''
Akhil did MBA in finance and he is very much interested in buying & selling stocks. He knows the price of a stock for the upcoming ‘n’ days. To maximize the profit he can sell or buy the stock any day. We need to help him to maximize the profit.

Input Format

Given the value of ‘n’ an array of size ‘n’ as input in two separate lines.

Constraints

1<= n <= 20

Output Format

Print the maximum earned profit.

Sample Input 0

4
2 8 1 5
Sample Output 0

10
Sample Input 1

4
0 -1 5 4
Sample Output 1

6
'''
n=int(input())
a=list(map(int,input().split()))[:n]
t,p=0,0
for i in range(n-1):
        if(a[i]<a[i+1]):
            p=a[i+1]-a[i]
            t = t+p
print(t)            