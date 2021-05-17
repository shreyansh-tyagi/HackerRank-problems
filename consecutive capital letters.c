/*
Kanishak got a task to find the two consecutive capital letters inside the string. If they exist return true else return false.

Input Format

Enter the string of size ‘n’.

Constraints

1<= n <= 20

Output Format

Print ‘Yes’ or ‘No’

Sample Input 0

arYAn
Sample Output 0

Yes
Sample Input 1

suDAma
Sample Output 1

Yes

*/
#include<stdio.h>
 
int main() {
   int u=0,i;
   char ch[80];
   scanf("%s",ch);
   i = 0;
   while (ch[i] != '\0') {
      if (ch[i] >= 'A' && ch[i] <= 'Z')
         u++;
      i++;
   }
 if(u>=2)
     printf("Yes");
 else
     printf("No");
   return (0);
}