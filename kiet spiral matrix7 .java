'''
Rahul want to solve the mystery i.e First he have to Convert the matrix into Spiral Form and the do it clockwise rotation.

if n=3

Spiral =>

1 2 3

8 9 4

7 6 5

Then do it Clockwise =>

7 8 1

6 9 2

5 4 3

Input Format

n=> It is the number i.e. n*n matrix format.

Constraints

1<=n<=25

Output Format

Print the desired matrix in spiral clock format.

Sample Input 0

3
Sample Output 0

7  8  1
6  9  2
5  4  3

'''
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
   Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int p=1;
         generateMatrix(n);
        // rotate(matrix);
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<n;j++){
        //         System.out.print(matrix[j][i]);
        //     }
        //     System.out.println();
        // }
    }
    public static void generateMatrix(int n) {
        int[][] result = new int[n][n];
        int cnt = 1;
        for (int layer = 0; layer < (n + 1) / 2; layer++) {
            // direction 1 - traverse from left to right
            for (int ptr = layer; ptr < n - layer; ptr++) {
                result[layer][ptr] = cnt++;
            }
            // direction 2 - traverse from top to bottom
            for (int ptr = layer + 1; ptr < n - layer; ptr++) {
                result[ptr][n - layer - 1] = cnt++;
            }
            // direction 3 - traverse from right to left
            for (int ptr = layer + 1; ptr < n - layer; ptr++) {
                result[n - layer - 1][n - ptr - 1] = cnt++;
            }
            // direction 4 - traverse from bottom to top
            for (int ptr = layer + 1; ptr < n - layer - 1; ptr++) {
                result[n - ptr - 1][layer] = cnt++;
            }
        }
         for(int i=0;i<n;i++){
            for(int j=n-1;j>=0;j--){
                System.out.print(result[j][i]+" ");
            }
            System.out.println();
        }
        
    }
}