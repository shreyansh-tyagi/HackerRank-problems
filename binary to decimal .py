def binaryToDecimal(n):
     num = n;
     dec_value = 0;
     
    # Initializing base
    # value to 1, i.e 2 ^ 0
     base = 1;
     
    temp = num;
    while(temp):
        last_digit = temp % 10;
        temp = int(temp / 10);
         
        dec_value += last_digit * base;
        base = base * 2;
    return dec_value;
 
# Driver Code
num = int(input());
print(binaryToDecimal(num));