'''
A Formula One race was organised by college sports club. All the participants were given a unique registration number. The registration number can be any positive number less than 1000000000. There were N rounds in the event. Each round can be won by only one participant and a single integer score is awarded to that participant. The final winner will be the participant having highest score in all the rounds. Given N pair of integers where ith pair represents the registration number of winner and score awarded to the winner in the ith round, find the final winner of the race.

Input Format

First line of the input contains a single integer N representing the number of rounds. Next N lines contains two integers each representing the registration number of winner and score awarded to the winner in that round. It is guaranteed that final winner will be unique.

Constraints

0< N <=100000

0< registration number <=1000000000

0< score <10000

Output Format

Print a single integer representing the registration number of the final winner

Sample Input 0

5
100 3
103456 5
100 2
35432 7
103456 4
Sample Output 0

103456
Explanation 0

The final scores will be –

100 – 5

103456 – 9

35432 – 7

'''
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int a[n][2];
    int max = 0, index = -1;
    for (int i = 0; i < n; i++)
    {
        cin>>a[i][0]>>a[i][1];
        if(a[i][1] > max)
        {
            max = a[i][1];
            index = i;
        }
    }
    cout<<a[index][0];
    
    return 0;
}