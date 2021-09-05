'''
Arjun was working on a research paper based on binary number system. He designed an algorithm to find maximum number of consecutive set bits in the binary array.

Binary array is an array that contains only 0’s & 1’s.

Input Format

Given the value of ‘n’ an array of size ‘n’ as input in two separate lines.

Constraints

1<= n <= 20

Output Format

Print the integer output.

Sample Input 0

4
0 0 0 0
Sample Output 0

0
'''
import java.util.*;

public class Solution {

  public static void main(String[] args) {

    Scanner yash = new Scanner(System.in);
    int n = yash.nextInt();
    int count = 0;
    int a[] = new int[n];
    for (int i = 0; i < n; i++) {
      a[i] = yash.nextInt();

    }
    for (int i = 0; i < n; i++) {
      if (a[i] == 0) {
        count = 0;
      } else if (a[i] == 1) {
        count++;
      }

    }
    System.out.print(count);
  }
}