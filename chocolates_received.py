child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]
def calculate_total_chocolates():
    sum1=0
    for total in chocolates_received:
        sum1=sum1+total
    return sum1
def reward_child(child_id_rewarded,extra_chocolates):
    if child_id_rewarded in child_id:
        if extra_chocolates>=1:
            for i in range(0,len(child_id)):
                if child_id[i]==child_id_rewarded:
                    chocolates_received[i]=chocolates_received[i]+extra_chocolates
                    print(chocolates_received)                   
        else:
            print("Extra chocolates is less than 1")
    else:
        print("Child id is invalid")

print(calculate_total_chocolates())
reward_child(20,2)
