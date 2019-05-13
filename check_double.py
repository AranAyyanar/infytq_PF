def check_double(number):
    temp=number+number
    temp=str(temp)
    temp1=str(number)
    length=len(temp1)
    count=0
    list1=[]
    list2=[]
    for i in temp1:
        list1.append(i)
    for j in temp:
        list2.append(j)
    for num_1 in list1:
        if num_1 in list2:
            count=count+1
    if count==length:
        return True
    else:
        return False
print(check_double(125874))
