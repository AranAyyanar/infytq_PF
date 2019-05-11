def calculate(distance,no_of_passengers):
    petrol_perlit=70
    mileage=10
    price_ticket=80
    distance_1=distance/mileage
    Total_price=price_ticket*no_of_passengers
    Total_petrol=petrol_perlit*distance_1
    if(Total_petrol<Total_price):
        profit=Total_price-Total_petrol
        return profit
    else:
        return -1
distance=5
no_of_passengers=10
print(calculate(distance,no_of_passengers))
