'''Prabhat is an addict. One day Anjali texted him a problem and she wants his reply in one word but the condition was the reply should be capitalised. Due to his addiction his hands keep shaking while typing.

Help Prabhat.

Input Format

A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 103.

Constraints

n<=103

Output Format

Output the given word after capitalization.

Sample Input 0

aicKED
Sample Output 0

AicKED '''

n=input()
print(n[0].upper()+n[1:])
