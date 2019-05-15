def find_ten_substring(num_str):
    list1=[]
    list2=[]
    list3=[]
    join=''
    for i in num_str:
        list1.append(int(i))
    for i in num_str:
        list2.append(i)
    for i in range(0,len(list1)):
        for j in range(0,len(list1)-i):
            sum1=sum(list1[i:(j+i)+1])
            if sum1==10:
                for f in range(i,(j+i)+1):
                    join=join+list2[f]
                list3.append(join)
                join=''
    return list3
     
num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
