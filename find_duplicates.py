def find_duplicates(list_of_numbers):
  list1=[]
  count=0
  list2=[]
  for i in list_of_numbers:
     for j in list_of_numbers:
       if i==j:
         count=count+1
     if count>1:
       list1.append(i)
       count=0
     else:
       count=0
  for i in list1:
     if i not in list2:
       list2.append(i)
  return list2

list_of_numbers=[1,2,2,3,3,3,4,4,4,4]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
