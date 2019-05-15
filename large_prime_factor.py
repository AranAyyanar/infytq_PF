def find_factors(num):
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    if(i==1):
        return True
    elif(num%i==0):
        return False;
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    list1=[]
    for num in list_of_factors:
        prime_num=is_prime(num,num//2)
        if (prime_num):
            list1.append(num)
        else:
            pass
    return max(list1)

def find_f(num):
    factors=find_factors(num)
    large=find_largest_prime_factor(factors)
    return large

def find_g(num):
    sum1=0
    for i in range(num,num+9):
        sum2=find_f(i)
        sum1=sum1+sum2
    return sum1
    
print(find_g(10))
