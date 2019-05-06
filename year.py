def generate_next_date(day,month,year):
    #Start writing your code here
    next_day=day
    next_month=month
    next_year=year
    if(year//4==0):
        if(year%100==0 and year%400==0):
            if(month==2 and day==29):
                next_day=1
                next_month=month+1
           
    else:
         if(month==2 and day==29):
                next_day=1
                next_month=month+1
    for i in range(1,13):
        if(day==31 and month%2!=0):
            next_day=1
            next_month=month+1
        elif(day==30 and month%2==0):
            next_day=1
            next_month=month+1
        elif(day==28 and month==2):
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
            
            
                
    print(next_day,"-",next_month,"-",next_year)


generate_next_date(29,2,2020)
