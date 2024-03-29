'''
In this challenge, we practice calculating the Pearson correlation coefficient. Check out the Tutorial tab for learning materials!

Task
Given two -element data sets,  and , calculate the value of the Pearson correlation coefficient.

Input Format

The first line contains an integer, , denoting the size of data sets  and .
The second line contains  space-separated real numbers (scaled to at most one decimal place), defining data set .
The third line contains  space-separated real numbers (scaled to at most one decimal place), defining data set .

Constraints

, where  is the  value of data set .
, where  is the  value of data set .
Data set  contains unique values.
Data set  contains unique values.
Output Format

Print the value of the Pearson correlation coefficient, rounded to a scale of  decimal places.

Sample Input

10
10 9.8 8 7.8 7.7 7 6 5 4 2 
200 44 32 24 22 17 15 12 8 4
Sample Output

0.612
Explanation

The mean and standard deviation of data set  are:

The mean and standard deviation of data set  are:

We use the following formula to calculate the Pearson correlation coefficient:

'''
N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

stdv_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5


covariance = sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))