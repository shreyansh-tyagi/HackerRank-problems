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

*
**
***

*/

#include<stdio.h>
int main()
{
    //clrscr();
    int i,j,n;
    scanf("%d",&n);
    if(n<=10){
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=i;j++)
        {
            printf("*");
        }
        
        printf("\n");
    }
    }
}
