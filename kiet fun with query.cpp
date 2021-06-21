/*
Vikas Bhayia likes to play with bits. One day Vikas bhayia decides to assign a task to his student Sanya. You have help Sanya to complete this task. Task is as follows - Vikas Bhayia gives Q queries each query containing two integers a and b. Your task is to count the no of set-bits in for all numbers between a and b (both inclusive)

Input Format

Read Q - No of Queries, Followed by Q lines containing 2 integers a and b.

Constraints

Q,a,b are integers.

Output Format

Q lines, each containing an output for your query.

Sample Input 0

3
1 1
10 15
10 11
Sample Output 0

1
17
5

*/
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
vector<int> change(int a)
{
    vector <int> v;
    for(int i=0;a>0;i++)
    {
        v.push_back(a%2);
        a = a/2;
    }
    return v;
}
int counting( vector<int> &a)
{
    int count=0;
    for(int i=0;i<a.size();i++)
    {
        if(a[i]==1)
            count++;
    }
    return count;
}
int main() {
    int q;
    cin>>q;
    vector <int> totalbit;
    while(q>0)
    {
        
        int a,b;
        cin>>a>>b;
        int count=0;
        while(a<=b)
        {
            int j=a;
            vector <int> c;
            c = change(j);
            count = count + counting(c);
            a++;
        }
        cout<<count<<endl;
        q--;
    }
    

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}