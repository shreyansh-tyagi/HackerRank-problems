'''
In designing a combinational circuit in Digital Logic Design (DLD), we use the elements like Multiplexers, Demultiplexers, Decoders etc. In this question we will consider the designing of Multiplexers only.

Multiplexer is a logical device with multiple inputs and only single output with select lines.

Ex: In a “ N X 1” multiplexer, we have N inputs, 1 output and ‘log N’ select lines.

We can implement a “M X 1” multiplexer using few “N X 1” multiplexers iff M > N. We ned to find that, how many level of design with multiplexers of size “N X 1” requires to develop a completely mature multiplexer of size “M X 1”. If not possible then print “Not Possible” as output.

Input Format

Input contains two integers M & N respectively.

Constraints

1 <= M <= 2000

1 <= N <= 1000

Output Format

Print the number of levels needed for mature implementation or “Not Possible”.

Sample Input 0

8 2
Sample Output 0

3
Sample Input 1

16 64
Sample Output 1

Not Possible
'''

import math
m,n=map(int,input().split())
if(m>n):
    a=math.sqrt(m)
    if(a==n):
        print('2')
    else:
        print('3')
    
else:
    print("Not Possible")