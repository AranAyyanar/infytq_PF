def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(food_type=="N"and quantity_ordered>0and distance_in_kms>0):
        if(quantity_ordered>=1):
            bill_amount=150*quantity_ordered
            for i in range(1,distance_in_kms+1):
                if(i>=1 and i<=3):
                    bill_amount=bill_amount
                elif(i>3 and i<=6):
                    bill_amount=bill_amount+3
                elif(i>6):
                    bill_amount=bill_amount+6
                else:
                    pass
    elif(food_type=="V"and quantity_ordered>0and distance_in_kms>0):
        if(quantity_ordered>=1):
            bill_amount=120*quantity_ordered
            for i in range(1,distance_in_kms+1):
                if(i>=1 and i<=3):
                    bill_amount=bill_amount
                elif(i>3 and i<=6):
                    bill_amount=bill_amount+3
                elif(i>6):
                    bill_amount=bill_amount+6
                else:
                    pass
    else:
        bill_amount=-1
    return bill_amount


bill_amount=calculate_bill_amount("N",1,7)
print(bill_amount)
