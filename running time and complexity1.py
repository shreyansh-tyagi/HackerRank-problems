'''
Today we will learn about running time, also known as time complexity. Check out the Tutorial tab for learning materials and an instructional video.

Task
A prime is a natural number greater than  that has no positive divisors other than  and itself. Given a number, , determine and print whether it is  or .

Note: If possible, try to come up with a  primality algorithm, or see what sort of optimizations you come up with for an  algorithm. Be sure to check out the Editorial after submitting your code.

Input Format

The first line contains an integer, , the number of test cases.
Each of the  subsequent lines contains an integer, , to be tested for primality.

Constraints

Output Format

For each test case, print whether  is  or  on a new line.

Sample Input

3
12
5
7
Sample Output

Not prime
Prime
Prime
Explanation

Test Case 0: .
 is divisible by numbers other than  and itself (i.e.: , , , ), so we print  on a new line.

Test Case 1: .
 is only divisible  and itself, so we print  on a new line.

Test Case 2: .
 is only divisible  and itself, so we print  on a new line.


''''
from math import sqrt
a=int(input())
def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True
for _ in range(a):
    n = int(input())
    
    if n >= 2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")