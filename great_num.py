def find_product(num1,num2,num3):
    product=0
    
    if(num1==7 or num2==7 or num3 ==7):
        if(num1==7):
            product=num2*num3
        elif(num2==7):
            product=num3
        else:
            product=-1
    else:
        product=num1*num2*num3
    return product

product=find_product(4,2,3)
print(product)
