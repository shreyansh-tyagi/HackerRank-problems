'''
Usser need to find out prime equliberium index of given number. prime equliberium index is based upon how far a number is from nearest prime number.

Input Format

single line input, only one integer(N)

Constraints

5<=N<=1000000000

Output Format

either positive or negetive integer

Sample Input 0

63
Sample Output 0

-2
Explanation 0

around prime number of 63 are 61 and 67 in both side. 61-63 = -2 67-63 = 4 so the nearest prime number is 61 and prime equliberium index is -2, if N is eqully distant from both prime numbers then positive equliberium index will be consider

'''
#include<bits/stdc++.h>
using namespace std;

bool isPrime(int n)
{
    for (int i = 2; i < n; i++)
    {
        if(n % i == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int n;
    cin>>n;
    int diff;
    int left = n - 1;
    int right = n + 1;
    if(isPrime(n))
    {
        cout<<0;
    }
    else
    {
        while(true)
        {
            if(isPrime(right))
            {
                diff = right - n;
                break;
            }
            else if(isPrime(left))
            {
                diff = left - n;
                break;
            }
            else
            {
                left--;
                right++;
            }
        }
        cout<<diff;
    }
    
    
    
    return 0;
}