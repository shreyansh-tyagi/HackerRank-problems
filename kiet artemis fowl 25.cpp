'''
Artemis is a skilled magician. He is very fond of playing with numbers and text. He is also a good reader. One day his taught him how to remeber new words.Artemis was given a book from which he was asked to count all randomly-generated string of characters ranging from a to z. But his father Artemis senior asked him to determine the number of subsequences that can be formed equal to this sequence 'abcdefghijklmnopqrstuvwxyz'. Now Artemis is having difficulty in doing the task. However his allowed to take help from one friend. You being Artemis's friends has to write a code to automate the task. Help Artemis win this task. Note: A subsequence is unique when at least a single character has its index that is different from all the other subsequences. Print the answer modulo 10^9+7(1000000007) for each test case in a new line.

Input Format

The first line will contain t denoting the number of test cases. The first line of each test case contains n denoting the size of the string. The second line of each test case contains string s of size n.

Constraints

1<=t<=10 1<=n<=100000 1<=|s|<=100000

Output Format

For each test case, print a single integer in a new line that denotes the count of number of unique subsequences that are possible as per the question.

Sample Input 0

3
27
abcdefghijklmnopqrstuvwxyzz
3
abz
28
abcdefghijklmnopqrstuvwxyyzz
Sample Output 0

2
0
4

'''
import java.util.*;
class Solution{

    // final 
    public static  void main(String args[]) {
        Scanner in = new Scanner(System.in);
        long mod = (long) (1e9) + 7;

        
        int t = in.nextInt();
        while (t--> 0) {
            int n = in.nextInt();
            char a[] = in.next().toCharArray();
            long dp[][] = new long[n + 1][27];
            for (int i = 0; i <= n; i++) dp[i][0] = 1;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= 26; j++) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j]) % mod;
                    int val = a[i - 1] - 'a';
                    if (val == j - 1) {
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod;
                    }
                }
            }

            System.out.println(dp[n][26]);
        }
    }
}