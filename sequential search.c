/*
Karan got a task to find the index of a particular element ‘k’. Help him out. In case of repeatetion print the index of first occurence of number.

Input Format

Enter the array of size ‘n’, element to search’k’, and array[] in three different lines.

Constraints

1<= n <= 20

Output Format

Print the index of element.

Sample Input 0

5
6
2 4 6 9 7
Sample Output 0

2

*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,a,i,j,b[40];
    scanf("%d",&n);
    scanf("%d",&a);
    for(i=0;i<n;i++)
        scanf("%d",&b[i]);
    for(j=0;j<n;j++)
    {
        if(a==b[j])
        {
        printf("%d",j);
        break;
        }
    }
    
    
    return 0;
}
