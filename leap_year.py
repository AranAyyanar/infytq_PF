def find_leap_years(given_year):
    list_of_leap_years=[]
    tst=given_year+100
    count=0
    for year in range(given_year,tst):
          if(year%4==0):
                if(year%100==0):
                    if(year%400==0):
                        list_of_leap_years.append(year)
                        count=count+1
                        if count==15:
                          break
                else:
                     list_of_leap_years.append(year)
                     count=count+1
                     if count==15:
                       break
    return list_of_leap_years

list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)
