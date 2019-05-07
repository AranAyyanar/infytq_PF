def find_sum_of_digits(number):
    sum_of_digits=0
    while(number!=0):
        remainder=number%10
        sum_of_digits=sum_of_digits+remainder
        number=number//10
    return sum_of_digits
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
