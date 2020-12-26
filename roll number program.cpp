/*Problem
Submissions
Leaderboard
Discussions
Suzy’s old friend ,Lucy, has come to meet her while she is in school. However, Lucy is only aware of Suzy’s roll number. Suppose A1, A2 … AN is the max roll number of Students in 1st, 2nd… Nth rooms respectively. So, students with roll number 1 to A1 are in room 1,, similarly in 2nd room students having roll number A[1] + 1 to A[2] … and students having roll number in Nth room will be from A[N-1] + 1 to A[N]. Help Lucy find out the room number where she can find Suzy.

Input Format

First line will contain N (No. of rooms). Next line will contain N space separated integers denoting Si, the number of students in ith room. Next line will contain Q (No. of queries). Then each next Q lines will contain Suzy’s roll number I.

Constraints

1 ≤ N, Q ≤ 10^5

Output Format

For every query, print in a new line : the room number in which she can find Suzy.

Sample Input 0

2
2 3
2
2
4
Sample Output 0

1
2
Explanation 0

First room will have students with roll number : 1, 2 Second room will have students with roll number : 3, 4, 5

Sample Input 1

4
3 4 5 3
2
5
12
Sample Output 1

2
3 */






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