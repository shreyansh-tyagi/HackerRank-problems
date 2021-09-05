'''
Print the given pattern for the given values of ‘N’.

Example: For N = 5

A

AB

A1C

A12D

A123E

Input Format

Input contains value of N.

Constraints

1 <= N <= 15

Output Format

Print the required pattern.

Sample Input 0

5
Sample Output 0

A
AB
A1C
A12D
A123E
Sample Input 1

4
Sample Output 1

A
AB
A1C
A12D

'''
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            if (j==1 || j==i)
                cout<<(char)(j+64);
            else
                cout<<j-1;
        }
        cout<<'\n';
    }
    
    return 0;
}