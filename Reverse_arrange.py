def encrypt_sentence(sentence):
    sentence=sentence.lower()
    flag=True
    f=len(sentence)
    for i in range(0,f-1):
        if sentence[i]==" "and sentence[i+1]==" ":
            flag=False
            break
        else:
            flag=True
    sentence=sentence.split(" ")
    if flag==True:
        for i in sentence:
            if i[0]>="a" and i[0]<="z":
                 flag=True
            else:
                 flag=False
                 break
    list1=[]
    list2=["a","e","i","o","u"]
    list3=[]
    join=''
    n=len(sentence)
    if flag==True :
       for i in range(1,n+1):
           if i%2!=0:
              for j in range(i-1,i):
                  k=sentence[j][::-1]
         	  list1.append(k)
      	   else:
              for j in sentence[i-1]:
                  if j not in list2:
                      join=join+j
                  else:
                      list3.append(j)
           for k in list3:
               join=join+k
           list1.append(join)
           list3=[]
           join=''
       l=" ".join(list1)
       return l

sentence="the iises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)
