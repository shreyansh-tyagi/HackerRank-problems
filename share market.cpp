/*
Akhil did MBA in finance and he is very much interested in buying & selling stocks. He knows the price of a stock for the upcoming ‘n’ days. To maximize the profit he can sell or buy the stock any day. We need to help him to maximize the profit.

Input Format

Given the value of ‘n’ an array of size ‘n’ as input in two separate lines.

Constraints

1<= n <= 20

Output Format

Print the maximum earned profit.

Sample Input 0

4
2 8 1 5
Sample Output 0

10
Sample Input 1

4
0 -1 5 4
Sample Output 1

6
*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,profit,i;
    cin>>n;
    int a[n];
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int totalprofit=0;
    for(i=0;i<n;i++)
    {
        if((i+1)<n)
        {
            if(a[i]<a[i+1])
            {
                profit = a[i+1]-a[i];
                totalprofit = totalprofit + profit;
            }
            
        }
    }
    cout<<totalprofit;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}
