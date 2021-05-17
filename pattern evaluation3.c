/*
Print the Pattern as given in sample cases.

Input Format

Enter the value ‘n’.

Constraints

1<= n <= 10

Output Format

Print respective pattern.

Sample Input 0

3
Sample Output 0

A
AB
ABC

*/

#include<stdio.h>
int main()
{
    
    int i,j,n;
    char ch[27]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    scanf("%d",&n);
    if(n<=10){
    for(i=0;i<=n;i++)
    {
        for(j=0;j<i;j++)
        {
            printf("%c",ch[j]);
        }
        
        printf("\n");
    }
    }
}
