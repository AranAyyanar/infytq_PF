def factorial(number):
    mul=1
    if number==0:
        return 1
    else:
        for i in range(number,0,-1):
            mul=mul*i
        return mul

def find_strong_numbers(num_list):
    sum1=0
    list1=[]
    for num in num_list:
        temp=num
        while temp>0:
            remainder=temp%10
            sum1=sum1+factorial(remainder)
            temp=temp//10
        if num==sum1:
            list1.append(num)
            sum1=0
        else:
            sum1
    return list1
num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
