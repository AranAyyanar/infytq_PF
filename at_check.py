def count_names(name_list):
    count1=0
    count2=0
    for i in name_list:
        if i.endswith("at") and not i.startswith("at"):
            count1=count1+1
    print("_at -> ",count1)
    for i in name_list:
        j=i.find("a")
        if i[j]=="a" and i[j+1]=="t":
            count2=count2+1
    print("%at% -> ",count2)
name_list=['hat', 'tat', 'tit', 'tatoo', 'gather']
count_names(name_list)
