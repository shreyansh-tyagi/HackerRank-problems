//Ramesh got a set of numbers and alloted a task to find the minimum of all the royal numbers present in the set if available otherwise print ‘No’. Royal numbers are those numbers which are divisible by 2,3 & 5 all three numbers.

Input Format

Enter all the numbers in the array of size ‘n’

Constraints

1<= n <= 20

Output Format

Print the minimum royal number.

Sample Input 0

32 30 62 90
Sample Output 0

30

//
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) 
    {
      Scanner sc = new Scanner(System.in);
     // int n=sc.nextInt();
      int a[]=new int[4];
      int i=0,flag=0,k=0;
      for(i=0;i<4;i++) a[i]=sc.nextInt();
      
      for(i=0;i<4;i++)
      {
        if(a[i]%2==0)
        {
         // flag++;
          
          if(a[i]%3==0) 
          {
           // flag++;
          
            if(a[i]%5==0) 
            {
              //flag++;
              k=a[i];
              break;
            }
          } 
        }
      }
      if( k!=0)System.out.print(k);
      else System.out.print("No");
    }
}