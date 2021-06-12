'''
As we all know, blockchain technology is mostly used to develop a decentralized application. 
A blockchain is a chain of connected block such that each block keeps the hash of its previous block.
You are given a list of blocks represented by pair of numbers. You have to find the maximum length that can be made by connecting these blocks.
The rule for connecting the blocks is:
Suppose a pair (x,y) is followed by (m,n). Then y must be less than m.

 

Input format:
First line contains n (number of pairs).
Each of the next n lines contains a and b separated by space of pair (a,b).
Every pair will be in the form (a,b) where a<b.
 

Output Format:
Print the maximum length of blockchain that can be made.

Constraint

SAMPLE INPUT 
5
5 24
39 60
15 28
27 40
50 90
SAMPLE OUTPUT 
3
Explanation
Longest chain would be formed by (5,24), (27,40) and (50,90)

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
c,d=[],[]
count=0
for i in range(n):
    a,b=map(int,input().split())
    c.append(a)
    d.append(b)    
for i in range(n-1):
    if(d[i]<c[i+1]):
        count+=1 
print(count+1)       

