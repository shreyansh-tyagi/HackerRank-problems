/*
C++ provides a nice alternative data type to manipulate strings, and the data type is conveniently called string. Some of its widely used features are the following:

Declaration:

string a = "abc";
Size:

int len = a.size();
Concatenate two strings:

string a = "abc";
string b = "def";
string c = a + b; // c = "abcdef".
Accessing  element:

string s = "abc";
char   c0 = s[0];   // c0 = 'a'
char   c1 = s[1];   // c1 = 'b'
char   c2 = s[2];   // c2 = 'c'

s[0] = 'z';         // s = "zbc"
P.S.: We will use cin/cout to read/write a string.

Input Format

You are given two strings,  and , separated by a new line. Each string will consist of lower case Latin characters ('a'-'z').

Output Format

In the first line print two space-separated integers, representing the length of  and  respectively.
In the second line print the string produced by concatenating  and  ().
In the third line print two strings separated by a space,  and .  and  are the same as  and , respectively, except that their first characters are swapped.

Sample Input

abcd
ef
Sample Output

4 2
abcdef
ebcd af
Explanation

 "abcd"
 "ef"
 "abcdef"
 "ebcd"
 "af"
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
  
  string s,s1,s2;
  cin>>s>>s1;
  int len=s.size();
  int len1=s1.size();
  cout<<len<<" "<<len1<<endl;
  cout<<s+s1<<endl;
  char temp;
  temp=s[0];
  s[0]=s1[0];
  s1[0]=temp;
  cout<<s<<" "<<s1;
  
  
    return 0;
}