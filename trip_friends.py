mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False

distance_one_way=distance_one_way*2
distance=distance_one_way/mileage
per_head_cost=distance*amount_per_litre
per_head_cost=per_head_cost/4
if per_head_cost%4==0:
    divisible_by_five=True

print(per_head_cost)
print(divisible_by_five)
