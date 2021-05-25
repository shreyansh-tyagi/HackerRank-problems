'''
Rashu got a task to match the characters inside the string. She got two different string as input and verify that if both have same length then the first three characters of both the strings are same or not. If same then print ‘Yes’ else print ‘No’.

Input Format

Enter two different strings of length ‘n’ separated by spaces.

Constraints

1<= n <= 20

Output Format

Print ‘Yes’ or ‘No’

Sample Input 0

aryan ary@@
Sample Output 0

Yes

'''
n,a=input().split(' ')
if(len(n)==len(a)):
    if(n[0:2]==a[0:2]):
        print('Yes')
    else:
        print('No')
else:
    print('No')