def find_smallest_number(num):
    count=0
    sum1=0
    for i in range(0,num+1):
        sum1=sum1+i
    for i in range(1,(1000*num)//10):
        for j in range(1,1000):
            if i%j==0:
                count=count+1
            else:
                continue
        if count==num:
            return i
            count=0
            break
        else:
            count=0
num=23
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)
