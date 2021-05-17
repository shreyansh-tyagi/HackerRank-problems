/*
Rishabh got a task to order the numbers in such a way that all got arrange in non-decreasing order. Write the necessart code to help him.

Input Format

Enter the size ‘n’ and array in two different lines.

Constraints

1<= n <= 20

Output Format

Print sorted array.

Sample Input 0

5
7 5 2 9 6
Sample Output 0

2 5 6 7 9

*/

#include<stdio.h>
int main()
{
    int i,j,a[50],n,temp=0;
    scanf("%d",&n);
    for(i=0;i<=n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if(a[i]<a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }

    }
      for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}
    
   
