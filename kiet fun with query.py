'''
Vikas Bhayia likes to play with bits. One day Vikas bhayia decides to assign a task to his student Sanya. You have help Sanya to complete this task. Task is as follows - Vikas Bhayia gives Q queries each query containing two integers a and b. Your task is to count the no of set-bits in for all numbers between a and b (both inclusive)

Input Format

Read Q - No of Queries, Followed by Q lines containing 2 integers a and b.

Constraints

Q,a,b are integers.

Output Format

Q lines, each containing an output for your query.

Sample Input 0

3
1 1
10 15
10 11
Sample Output 0

1
17
5

'''

a=int(input())
def decimalToBinary(n):
    return bin(n).replace("0b", "")
for i in range(a):
    b,c=map(int,input().split())
    f=0
    for j in range(b,c+1):
        d=decimalToBinary(j)
        e=str(d)
        c=[]
        for i in range(len(e)):
            c.append(e[i])   
        f+=c.count('1')
        c.clear()
    print(f)    
        
        
        
        