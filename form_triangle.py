def form_triangle(num1,num2,num3):
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    count=0
    list=[0,0,0]
    list1=[0,0,0]
    list1[0]=num3
    list1[1]=num2
    list1[2]=num1
    num4=num1+num2
    list[0]=num4
    num5=num1+num3
    list[1]=num5
    num6=num2+num3
    list[2]=num6
    for index in range(0,len(list)):
        if (list[index]>list1[index]):
            count=count+1
                
    if count==3:
        return success
    else:
        return failure
