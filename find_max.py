def find_max(num1, num2):
    max_num=-1
    sum=0
    count=0
    list1=[]
    
    if(num1<num2):
        for number in range(num1,num2+1):
            temp=number
            while temp>0:
                remainder=temp%10
                sum=sum+remainder
                temp=temp//10
                count=count+1
            if(sum%3==0 and count==2 and number%5==0):
                list1.append(number)
                max_num=max(list1)
            else:
                count=0
                sum=0
            
    else:
        max_num=max_num
    return max_num
