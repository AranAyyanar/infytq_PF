def merge_lists(list1,list2):
    new_merge_list=list1+list2

    return new_merge_list
def sort_list(merged_list):
    for i in range(0,len(merged_list)):
        for j in range(i+1,len(merged_list)):
            if merged_list[i]==merged_list[j]:
                temp=merged_list[j]
                merged_list[j]=merged_list[i+1]
                merged_list[i+1]=temp
    
            elif merged_list[i]>merged_list[j]:
                temp=merged_list[j]
                merged_list[j]=merged_list[i]
                merged_list[i]=temp
    return merged_list
merged_list=merge_lists(list1=[4,0,-2,3,-1] ,list2=[])
print(merged_list)
sorted_merged_list=sort_list(merged_list)
print(sorted_merged_list)
