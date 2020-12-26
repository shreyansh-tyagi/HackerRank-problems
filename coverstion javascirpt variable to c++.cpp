#include<bits/stdc++.h>
using namespace std;

int main()
{
    string s;
    cin>>s;
    string word = "";
    int l = s.length();
    for(int i = 0; i < l; i++)
    {
        char c = s.at(i);
        if( (int)c > 90)
        {
            word = word + c;
        }
        else
        {
            word = word + '_' + (char)((int)c + 32);
        }
    }
    cout<<word<<'\n';
    return 0;
}