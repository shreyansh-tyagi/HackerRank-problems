/*
Rishabh got a task to find multiply two 1-D array in such a way that only relative element get multiplied.

Input Format

Enter the two arrays in two different lines of size ‘n’.

Constraints

1<= n <= 20

Output Format

Print the array obtained after multiplying both.

Sample Input 0

1 2 3 4
2 3 4 5
Sample Output 0

2 6 12 20
Sample Input 1

1 2 3 4
1 2 3 4
Sample Output 1

1 4 9 16
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int i,j,a[50],b[50];
    for(i=0;i<4;i++)
        scanf("%d",&a[i]);
    for(j=0;j<4;j++)
        scanf("%d",&b[j]);
    for(j=0;j<4;j++)
        printf("%d ",a[j]*b[j]);
    return 0;
}

