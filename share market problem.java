'''
Akhil did MBA in finance and he is very much interested in buying & selling stocks. He knows the price of a stock for the upcoming ‘n’ days. To maximize the profit he can sell or buy the stock any day. We need to help him to maximize the profit.

Input Format

Given the value of ‘n’ an array of size ‘n’ as input in two separate lines.

Constraints

1<= n <= 20

Output Format

Print the maximum earned profit.

Sample Input 0

4
2 8 1 5
Sample Output 0

10
Sample Input 1

4
0 -1 5 4
Sample Output 1

6

'''
import java.io.*;
import java.util.*;

public class Solution {

  public static void main(String[] args) {
    Scanner neww = new Scanner(System.in);
    int sum = 0;
    int n = neww.nextInt();

    int profit, i, j;

    int a[] = new int[n];

    for (i = 0; i < n; i++)
      a[i] = neww.nextInt();

    for (i = 0; i < n; i++) {
      if ((i + 1) < n) {
        if (a[i] < a[i + 1]) {
          profit = a[i + 1] - a[i];
          sum = sum + profit;
        }
      } else
        break;
    }
    System.out.print(sum);
  }
}