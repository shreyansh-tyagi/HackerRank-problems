'''
Ramesh got a set of numbers and alloted a task to find the minimum of all the royal numbers present in the set if available otherwise print ‘No’. Royal numbers are those numbers which are divisible by 2,3 & 5 all three numbers.

Input Format

Enter all the numbers in the array of size ‘n’

Constraints

1<= n <= 20

Output Format

Print the minimum royal number.

Sample Input 0

32 30 62 90
Sample Output 0

30
'''
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(len(a)):
    if((a[i]%2==0)and(a[i]%3==0)and(a[i]%5==0)):
        b.append(a[i])

if(min(b)!=0):
    print(min(b))
else:
    print('No')