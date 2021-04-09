/**Ravi wants to propose Anjali but Anjali loves Half PATTERNS. Anjali will only accept the proposal if Ravi gifts the best PATTERN to her. Ravi bought the 'Heart of the Ocean' the most expensive HALF diamond for Anjali but now he need Rs 55 to buy a diamond shaped gift wrapper.As his friend you have to help Ravi by building a diamond shaped gift wrapper so he can print it out, wrap it up and gift it to Anjali.

Input Format

Input contains only one thing n.

Constraints

n<=10

Output Format

Obtain that PATTERN

Sample Input 0

3
Sample Output 0

******
**  **
*    *

**/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
int n,i,j,k,x;
scanf("%d",&n);
for(i=1;i<=n;i++)
{
for(j=n;j>=i;j--)
{
printf("*");
}
for(k=1;k<i;k++)
{
printf("  ");
}
for(x=n;x>=i;x--)
{
printf("*");
}
printf("\n");
}


    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}