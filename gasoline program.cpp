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