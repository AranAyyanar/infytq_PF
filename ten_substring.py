def find_ten_substring(num_str):
    list1=[]
    list2=[]
    for i in num_str:
        list1.append(int(i))
    for j in range(0,len(list1)-1):
        if (list1[j]+list1[j+1])==10:
            join=str(list1[j])+str(list1[j+1])
            list2.append(join)
    for j in range(0,len(list1)-2):
        if (list1[j]+list1[j+1]+list1[j+2])==10:
            join=str(list1[j])+str(list1[j+1])+str(list1[j+2])
            list2.append(join)
    for j in range(0,len(list1)-3):
        if (list1[j]+list1[j+1]+list1[j+2]+list1[j+3])==10:
            join=str(list1[j])+str(list1[j+1])+str(list1[j+2])+str(list1[j+3])
            list2.append(join)
    for j in range(0,len(list1)-4):
        if (list1[j]+list1[j+1]+list1[j+2]+list1[j+3]+list1[j+4])==10:
            join=str(list1[j])+str(list1[j+1])+str(list1[j+2])+str(list1[j+3])+str(list1[j+4])
            list2.append(join)
    return list2

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
