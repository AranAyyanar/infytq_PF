def create_largest_number(number_list):
    for i in range(0,len(number_list)):
        for j in range(i+1,len(number_list)):
            if number_list[i]==number_list[j]:
                temp=number_list[j]
                number_list[j]=number_list[i+1]
                number_list[i+1]=temp
            elif number_list[i]<number_list[j]:
                temp=number_list[j]
                number_list[j]=number_list[i]
                number_list[i]=temp
    join=""
    for num in number_list:
        num=str(num)
        join=join+num
    join=int(join)
    return join
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
