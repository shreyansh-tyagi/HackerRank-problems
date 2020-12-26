/*Let suppose N cars are parked on a circular track**(1 to N)** at distance of 1km each. Each car contains some fuels (Fi to Fn).A car runs 2km per litre of fuel. You are driving car 1 in the clockwise direction. To move one unit of distance in this direction, you need to spend half litre of gasoline. When you pass another car parked at even position (even if you'd run out of gasoline exactly at that point), you steal all its gasoline and When you pass another car parked at odd position,you steal half of its gasoline each time. Once you do not have any gasoline left, you stop.

Here is one catch that you will not steal gasoline from other cars if that car has less then 2 litres of gasoline.

What is the total clockwise distance travelled by your car?

Input Format

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.

The first line of each test case contains a single integer N.

The second line contains N space-separated integers f1,f2,…,fN.

Constraints

1≤ T ≤100

1≤ N ≤100

0≤ fi ≤100

Output Format

Total distance traveled for each test cases into seperated line.

Sample Input 0

2
5
1 2 3 4 5
6
2 5 2 0 1 0
Sample Output 0

 24.5
 16 */

#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<float> v(n);

        for(int i = 0; i < n; i++)
            cin>>v[i];

        float gas = v[0]; v[0] = 0;
        float distance = 0;
        while(gas >= 0)
        {
            gas = gas - 0.5;
            distance++;
            for(int i = 1; i < n; i++)
            {
                gas = gas - 0.5;
                distance++;
                if(gas >= 0)
                {
                    if(v[i] >= 2)
                    {
                        if( (i+1) % 2 == 0)
                        {
                            gas += v[i];
                            v[i] = 0;
                        }
                        else
                        {
                            gas = gas + v[i]/2;
                            v[i] = v[i]/2;
                        }
                    }
                }
                else
                    break;
            }
        }
        cout<< " ";
        cout<< gas*2 + distance << '\n';
    }
    return 0;
}