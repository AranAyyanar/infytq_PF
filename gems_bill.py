def gems_bill(reqd_gems,reqd_quantity,price_list,gems_list):
    bill_amount=0
    for index in range(0,len(reqd_gems)):
        for index2 in range(0,len(gems_list)):
            if reqd_gems[index]==gems_list[index2]:
                bill_amount=bill_amount+(price_list[index2]*reqd_quantity[index])
    return bill_amount
                
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    for index in range(0,len(reqd_gems)):
        if reqd_gems[index] in gems_list:
            bill_amount=gems_bill(reqd_gems,reqd_quantity,price_list,gems_list)
        else:
            bill_amount=-1
            break
    if bill_amount>30000:
        discount=(5/100)*bill_amount
        bill_amount=bill_amount-discount
        return bill_amount
    else:
        return bill_amount


gems_list=['Amber', 'Aquamarine', 'Opal', 'Topaz']
price_list=[4316, 1342, 8734, 6421]
reqd_gems=['Amber', 'Topaz']
reqd_quantity=[1, 4]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
