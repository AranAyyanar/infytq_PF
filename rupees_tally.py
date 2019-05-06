
def rupees(temp,no_of_one,one_needed,rupees_to_make):
     for i in range(1,no_of_one+1):
            temp=temp+1
            if(temp<=rupees_to_make):
               one_needed=one_needed+1
     print("No. of One needed  :", one_needed)
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    sum=0
    temp=0
    total=(5*no_of_five)+(1*no_of_one)
    if(total>=rupees_to_make):
        
        for i in range(1,no_of_five+1):
            sum=sum+5
            if(sum<=rupees_to_make):
                    five_needed=five_needed+1
                    temp=sum
        if((temp+no_of_one)>=rupees_to_make):
             print("No. of Five needed :", five_needed)
             rupees(temp,no_of_one,one_needed,rupees_to_make)
        else:
            print(-1)
        
    else:
        print(-1)
    

make_amount(93,19,2)
