def nearest_palindrome(number):
    number=number+1
    flag=False
    sum1=0
    while flag==False:
        temp=number
        while temp!=0:
            remainder=temp%10
            sum1=(sum1*10)+remainder
            temp=temp//10
        if sum1==number:
            flag=True
        else:
            number=number+1
            sum1=0
    return number
    
    
number=99
print(nearest_palindrome(number))
