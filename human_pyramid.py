def human_pyramid(no_of_people):
    if no_of_people==1:
        return 1*50
    else:
        return no_of_people*50+human_pyramid(no_of_people-2)
def find_maximum_people(max_weight):
    total=max_weight//50
    no_of_people=0
    sum1=0
    for i in range(1,total+1,2):
        sum1=sum1+(i*50)
        if sum1<=max_weight:
            no_of_people=i
    return no_of_people
    
max_people=find_maximum_people(1000)
print(max_people)
