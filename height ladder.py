'''
You have to arrange student in height wise.There will be some student whom height will be same so u have to arrange all of them in a beautiful line.

The first line of each test case contains an Integer 'N' denoting the number of the student.

The second line of each test case contains 'N' space-separated Integers denoting the height of students.

For each test case, print a line in which students are arranged in a beautiful line in heightwise manner.

SAMPLE INPUT 
10
2 2 1 1 2 0 2 0 2 1
SAMPLE OUTPUT 
0 0 1 1 1 2 2 2 2 2
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
n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
for i in a:
    print(i,end=' ')