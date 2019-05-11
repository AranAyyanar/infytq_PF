def celsius(degree):
    celsius_value=(degree-32)*(5/9)
    return celsius_value
def fahrenheit(degree):
    fah_value=(degree*(9/5))+32
    return fah_value

def convert(degree,to_covert):
    if to_covert=="celsius":
        value=celsius(degree)
        print(value)
    elif(to_covert=="fahrenheit"):
        value=fahrenheit(degree)
        print(value)
    else:
        print("Invalid")
covertion=convert(15,"fahrenheit")
