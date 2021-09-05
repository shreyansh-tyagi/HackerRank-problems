'''
Vikas Bhayia likes to play with bits. One day Vikas bhayia decides to assign a task to his student Sanya. You have help Sanya to complete this task. Task is as follows - Vikas Bhayia gives Q queries each query containing two integers a and b. Your task is to count the no of set-bits in for all numbers between a and b (both inclusive)

Input Format

Read Q - No of Queries, Followed by Q lines containing 2 integers a and b.

Constraints

Q,a,b are integers.

Output Format

Q lines, each containing an output for your query.

Sample Input 0

3
1 1
10 15
10 11
Sample Output 0

1
17
5

'''
import java.io.*;
import java.util.*;

public class Solution {
    public static int binaryCount(int n)
    {
        int count = 0;
        while (n > 0) {
            count =count+1;
            n = n & (n-1);
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        for(int j=0;j<x;j++)
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int total=0;
            for(int i=a;i<=b;i++)
            {
                total += binaryCount(i);
            }
            System.out.println(total);
        }
        
    }
}