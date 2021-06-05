'''
Internal nodes are those nodes of tree that have atleast one child and the node with no child called as leaf. N-ary tree is a tree in which a node can have maximum of n-child.

We have a n-ary tree with X internal nodes. Find the maximum number of leaf nodes present in that tree.

Ex- Binary tree with 3 internal nodes can have maximum of 4 leaf nodes. Similarly ternary(3-ary) with 5 internal nodes can have maximum of 11 leaf nodes. Generalise the concept and find out the the number of leaf nodes for various n-ary tree with different internal nodes.

Input Format

Input the value of n & X respectively

Constraints

1 <= n <= 10

1 <= X <= 25

Output Format

Print the number of leafs.

Sample Input 0

2 3
Sample Output 0

4
Sample Input 1

3 5
Sample Output 1

11
Submissions: 13
Max Score: 10
Difficulty: Hard
Rate This Challenge:

    
More
 
1
​
'''


a,b=map(int,input().split())
print(((a*b)-(b-1)))