'''
Bob has just turned 18 years old and has opened a Bank account. However, since he has just opened his bank account he is not very experienced about the working of banks, therefore he asks for your help. Bob wants to know whether the IFSC Code given by the bank is valid or not, can you help him? A valid IFSC (Indian Financial System) Code must be of the following format:- 1) The string should be 11 characters long. 2) The first four characters of the IFSC Code should be upper case alphabets. 3) The fifth character should be 0. 4) The last six characters should be alphanumeric.

SAMPLE INPUT 
59587947263620425540520450385RFJHQ
SAMPLE OUTPUT 
False
'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=input()
b=n[:4]
b=b.upper()
if len(n)==11 and n[:4]==b and n[4]=='0' and n[5:].isalnum():
    print('True') 
else:
    print('False')   
