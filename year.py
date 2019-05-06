def leapyear(year,month,day):
    if(year%4==0):
        if(year%100==0 and year%400==0):
            if(day==28):
                next_day=day+1
                return next_day
        else:
            next_day=day+1
            return next_day
    else:
        next_day=1
        return next_day
def generate_next_date(day,month,year):
    next_day=day
    next_month=month
    next_year=year
    if(month>=1 and month<=7):
        if(day==31 and month%2!=0):
            next_day=1
            next_month=month+1
        elif(day==30 and month%2==0):
            next_day=1
            next_month=month+1
        elif(month==2):
            if(day==29):
                next_day=1
                next_month=month+1
            else:
                ret_val=leapyear(year,month,day)
                next_day=ret_val
                if(next_day==1):
                    next_month=month+1
                else:
                    next_month=month
        else:
            next_day=day+1
    elif(month>=8 and month<=12):
        if(day==31 and month%2==0):
            if(month==12):
                next_day=1
                next_month=1
            else:
                next_day=1
                next_month=month+1
                
        elif(day==30 and month%2!=0):
            next_day=1
            next_month=month+1
        else:
             next_day=day+1    
    print(next_day,"-",next_month,"-",next_year)
generate_next_date(28,2,2019)
