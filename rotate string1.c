/*
Karan got a task to left rotate a string by one place. You need to help him by designing an algorithm that gives the second letter of rotated string

Input Format

Enter the string of size ‘n’.

Constraints

1<= n <= 20

Output Format

Print the letter.

Sample Input 0

aryan
Sample Output 0

y
*/
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    char ch[30];
    scanf("%s",ch);
    int count=0,i=0;
    while(ch[i]='\0')
    {
        count++;
        i++;
    }
    ch[0]=ch[count+1];
    printf("%c",ch[2]);
    
}
