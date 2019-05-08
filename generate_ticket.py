def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    auto_num=100
    for num_tic in range(1,no_of_passengers+1):
        dest=destination[0:3]
        sour=source[0:3]
        auto_num=auto_num+1
        num=str(auto_num)
        tick_ent=airline+":"+sour+":"+dest+":"+num
        ticket_number_list.append(tick_ent)
    if no_of_passengers>5:
         tick_print=len(ticket_number_list)-5
         return ticket_number_list[tick_print:]
    else:
        return ticket_number_list
print(generate_ticket("AI","Bangalore","London",10))
