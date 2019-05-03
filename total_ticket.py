def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    rate_per_adult=37550
    rate_per_child=rate_per_adult/3
    service_tax=7/100
  
    total_ticket_cost=(no_of_adults*rate_per_adult)+(no_of_children*rate_per_child)
    service_tax=total_ticket_cost*service_tax
    total_ticket_cost=total_ticket_cost+service_tax
    discount=10/100
    discount=total_ticket_cost*discount
    total_ticket_cost=total_ticket_cost-discount

    return total_ticket_cost
total_ticket_cost=calculate_total_ticket_cost(3,47)
print("Total Ticket Cost:",total_ticket_cost)
