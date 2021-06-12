'''
Keshari is a DAPPS enthusiast. He works in a company where he builds the App using the smart contract for 2 clients, A and B. Both Clients have different expectations and specifications, but both pay the same, 1 Ethereum coin for every App.
Client A wants that you build the App with 2 instances of custom server and 1 instance of cloud server, Where Client B wants the App to have 1 instance of custom server and 2 instances of cloud servers. Keshari can only provide limited number of server instances, that is,   instances of custom servers and  instances of cloud servers.

Find out the maximum Ethereum coins Keshari can earn.

Input Format:
First Line contains t, no. of test cases
Second line contains two space separated integers  (max. no of custom and cloud servers keshari can provide).
Output Format
•   For each testcase, print the maximum number of Ethereum coins Keshari can earn.

 

Constraint

SAMPLE INPUT 
4
8 7
10 0
7 15
4 4
SAMPLE OUTPUT 
5
0 
7 
2
Explanation
In the first testcase, he has 8  instances of custom servers and 7 instances of cloud servers. He can make 3 Apps for Client A, (6 Custom + 3 cloud) and 2 Apps for Client B (2 Custom + 4 Cloud), earning him 5 coins.

In 2nd testcase he does not have any cloud server, so he can't earn anything

In 3rd testcase, he can earn 7 coins (By Making 7 Apps for Client B).

in 4th testcase, he can earn 2 coins, By making 2 Apps for Client A,or 1 for A and 1 for B. Either way, 2 coins is max he is going to earn.

Time Limit:	0.5 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Score is assigned when all the testcases pass.
Allowed Languages:	Bash, C, C++, C++14, C++17, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8, Java 14, JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl, PHP, Python, Python 3, Python 3.8, R(RScript), Racket, Ruby, Rust, Scala, Swift-4.1, Swift, TypeScript, Visual Basic

'''


n=int(input())
count=0
for i in range(n):
    a,b=map(int,input().split())
    if(a and b>0):
        while(a!=0 and b!=0):
            if(a>b):
                a=a-2
                b=b-1
                count+=1
            elif(a<b):
                a=a-1
                b=b-2
                count+=1
            else:
                print(count-1)        
        print(count)
    else:
        print('0')    
    count=0        









