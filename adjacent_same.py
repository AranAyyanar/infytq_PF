def get_count(num_list):
    count=0
    Total_element=len(num_list)
    for num in range(0,Total_element):
        if(num_list[num]==num_list[num+1]):
            count=count+1
            if((num+2)==Total_element):
                break
        else:
            if((num+2)==Total_element):
                break
            else:
                pass
    return count
num_list=[98,97,97,98]
print(get_count(num_list))
