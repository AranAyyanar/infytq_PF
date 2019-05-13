menu=('Veg Roll','Noodles','Fried Rice','Soup')
quantity_available=[2,200,3,0] 

def place_order(*item_tuple):
    count=1
    for i in item_tuple[0::2]:
        if i in menu:
            pass
        else:
            print(i+ " is not available")
    for index1 in range(0,len(item_tuple),2):
        for index in range(0,len(menu)):
            if item_tuple[index1]==menu[index]:
                quantity_requested=item_tuple[count]
                available=check_quantity_available(index,quantity_requested)
                if (available):
                    print (menu[index]+" is available")
                    count=count+2
                else:
                    print(menu[index]+" stock is over")
                    count=count+2
def check_quantity_available(index,quantity_requested):
        if quantity_requested<=quantity_available[index]:
            quantity_available[index]=quantity_available[index]-quantity_requested
            return True
        else:
            return False

place_order('Fried Rice',2,'Soup',1 )
