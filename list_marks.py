list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum1=0
    count=0
    for marks in list_of_marks:
        if marks>=10:
            sum1=sum1+marks
    sum1=sum1//10
    for marks in list_of_marks:
        if marks>=sum1:
            count=count+1
    average=count*10
    return average
def sort_marks():
    list1=[]
    for marks2 in list_of_marks:
        list1.append(marks2)
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                temp=list1[j]
                list1[j]=list1[i+1]
                list1[i+1]=temp
            elif list1[i]>list1[j]:
                temp=list1[j]
                list1[j]=list1[i]
                list1[i]=temp
    return list1

def generate_frequency():
    list3=[0 for i in range(0,25)]
    for marks3 in list_of_marks:
        for j in range(0,25):
            if j==marks3:
                list3[j]=list3[j]+1
                break
    return list3
        
print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
