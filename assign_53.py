data="hi Is is herb"
data=data.lower()
list1=data.split(" ")
count=0
list2=[] #repeat words
list3=[] # count
list4=[] #taking single value of repeat
list5=[] #taking count for that value
list6=[] 
for i in list1:
  for j in list1:
    if i==j:
      count=count+1
  if count>=1:
    list2.append(i)
    list3.append(count)
    count=0
  else:
    count=0
for i in list2:
  j=list2.index(i)
  if i not in list4:
    list4.append(i)
    list5.append(list3[j])
l=max(list5)
for i in range(0,len(list5)):
  if list5[i]==l:
    count=count+1
if count>1:
  for i in list4:
    g=len(i)
    list6.append(g)
  o=max(list6)
  m=list6.index(o)
  for i in range(0,len(list4)):
    if list4[i]==list4[m]:
      print(list4[i],end=' ')
      print(list5[i])
else:
  f=max(list5)
  m=list5.index(f)
  for i in range(0,len(list4)):
    if list4[i]==list4[m]:
      print(list4[i],end=' ')
      print(list5[i])
