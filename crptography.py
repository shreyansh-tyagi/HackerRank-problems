'''

There are many types of cryptography. One of them is Asymmetric key cryptography, which works on two different keys, public keys and private keys. 
Any text can be encrypted using a public key and decrypted using a private key.
For a given public key and a string, you have to encrypt the string.
A public key consists of two numbers, n and e.
The string contains only numeric digits, which represents a number.


You are given n, e and string s. Encrypt the string using formula   (Here % denotes Modulus Operator)

 

Input Format:
First line contains n and e (space separated)

Second Line contains s (string to be encrypted)

Output Format:
Print the encrypted string

Constraint:

 

 

 

 

SAMPLE INPUT 
3127 3
89
SAMPLE OUTPUT 
1394
Explanation
(89^3) mod 3127 = 1394

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned when all the testcases pass.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
a,b=map(int,input().split())
c=input()
if (a<pow(10,5)and(b<pow(10,9)and(len(c)<10))):
    d=pow(int(c),b)
    e=d%a
    print(e)
