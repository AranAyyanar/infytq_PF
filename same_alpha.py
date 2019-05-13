def find_common_characters(msg1,msg2):
    list1=[]
    list2=[]
    join=""
    for m1 in msg1:
        for m2 in msg2:
            if m1==m2:
                list1.append(m1)
    for alpha in list1:
        if alpha not in list2 and alpha!=" ":
            list2.append(alpha)
    if list2==[]:
        join=-1
    else:
        for final in list2:
            join=join+final
            
    return join
msg1="Apple"
msg2="Moto"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
