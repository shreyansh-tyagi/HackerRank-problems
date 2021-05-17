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
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
      int n=sc.nextInt();
      
      char i;
      char j;
      for(i='A';i<='A'+n-1;i++)
      {
        for(j='A';j<=i;j++)
        {
          System.out.print(j);
        }
        System.out.print("\n");
      }
    }
}
