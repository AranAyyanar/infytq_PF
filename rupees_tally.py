def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    sum=0
    temp=0
    total=(5*no_of_five)+(1*no_of_five)
    if(total>=rupees_to_make):
        
        for i in range(1,no_of_five+1):
            sum=sum+5
            if(sum<=rupees_to_make):
                    five_needed=five_needed+1
                    temp=sum
        print('No. of Five needed :')
        print(five_needed)
        for i in range(1,no_of_one+1):
            temp=temp+1
            if(temp<=rupees_to_make):
               one_needed=one_needed+1
        print('No. of One needed :')
        print(one_needed)
    else:
        print(-1)
make_amount(21,4,2)
