def human_pyramid(no_of_people,max_weight):
    sum1=no_of_people*50
    flag=True
    while flag==True:
        if sum1<max_weight and no_of_people%2!=0:
            no_of_people=no_of_people
            print(sum1)
            flag=False
        else:
            no_of_people=no_of_people-1
            sum1=sum1-50
    return no_of_people
def find_maximum_people(max_weight):
    no_of_people=int(max_weight/50)
    weight=human_pyramid(no_of_people,max_weight)
    return weight
max_people=find_maximum_people(1050)
print(max_people)
