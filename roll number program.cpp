#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, query;
    cin>>n;
    vector<int> a(n);
    for(int i = 0; i < n; i++)
        cin>>a[i];
    cin>>query;
    while(query > 0)
    {
        int rol;
        cin>>rol;
        int sum = 0, roomNo = 0;
        for(int i = 0; i < n; i++)
        {
            sum = sum + a[i];
            if(rol <= sum)
            {
                roomNo = i + 1;
                break;
            }
        }
        query--;
        cout<<roomNo<<'\n';
    }
    return 0;
}