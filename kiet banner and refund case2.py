'''
Banner is a criminal he buys item from amazon and pretends like he didnt received it in the first place. After looting amazon for a year Banner starts his own shop and accepts only Rs. 5, Rs. 10 and Rs. 15. An item costs Rs. 5.

There are N people (numbered 1 through N) standing in a queue to buy items. Each person wants to buy exactly one item. For each valid i, the i-th person has one coin with value a[i]. It is only possible for someone to buy an item when Banner can give them back their change exactly ― for example, if someone pays with a Rs. 10 coin, Banner needs to have a Rs. 5 coin that he gives to this person as change.

Initially, Banner has no money. He wants to know if he can sell items to everyone in the queue, in the given order. If he is not able to give back the change to a customer, the customer will call the police and Banner will be caught and executed for all the crimes he did.

Input Format

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N. The second line contains N space-separated integers a1,a2,…,aN.

Constraints

1≤T≤100

1≤N≤103

a[i] ∈ {5,10,15} for each valid i

Output Format

Print "NO" if banner will be executed or "YES" if he is safe. (without double quotes)

Sample Input 0

3
2
5 10
2
10 5
2
5 15
Sample Output 0

YES
NO
NO

'''
#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin>>v[i];
        }
        int five = 0, ten = 0, fifteen = 0, flag = 1;
        for (int i = 0; i < n; i++)
        {
            if (v[i] == 5)
            {
                five++;
            }
            else if (v[i] == 10 && five > 0)
            {
                ten++;
                five--;
            }
            else if (v[i] == 15 && (ten > 0 || five > 1) )
            {
                if (ten > 0)
                    ten--;
                else
                    five-=2;
                fifteen++;
            }
            else
            {
                flag = -1;
                break;
            }
        }
        if (flag == -1)
            cout<<"NO"<<'\n';
        else
            cout<<"YES"<<'\n';
    }
    return 0;
}