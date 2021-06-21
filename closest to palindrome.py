'''
Find the closest palindrome number to the input number.

If input number is palindrome then print that number in output.

If two palindrome numbers tie in absolute distance, print the smaller number in output.

Input Format

Input consists an integer N.

Constraints

0<=N<=10000 0<=Palindrome Number<=9999

Output Format

Output consists a palindrome number which is closest to N.

Sample Input 0

121
Sample Output 0

121
'''


f=int(input())
n,e=f,f
a,b,c,d=0,0,0,0
if str(n)==str(n)[::-1]:
    print(n)
else:
    while(True):
        n+=1
        if str(n)==str(n)[::-1]:
            a=n
            break
        c+=1    
if str(e)!=str(e)[::-1]:
    while(True):
        e-=1
        if str(e)==str(e)[::-1]:
            d=e
            break
        b+=1   
if str(f)!=str(f)[::-1]:
    if(c<b):
        print(a)
    else:
        print(d)	