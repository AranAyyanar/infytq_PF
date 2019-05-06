def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    if(food_type=="N"):
        if(quantity_ordered>=1):
            bill_amount=150*quantity_ordered
            for i in range(0,distance_in_kms+1):
                if(i<=3):
                    bill_amount=bill_amount
                elif(i>3 and i<=6):
                    bill_amount=bill_amount+((i-3)+3)
                elif(i>6):
                    bill_amount=bill_amount+((i-6)+6)
                else:
                    bill_amount=-1
    return bill_amount


bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)
