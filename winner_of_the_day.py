def find_winner_of_the_day(*match_tuple):
    count1=0
    count2=0
    for teams in match_tuple:
        if teams=="Team1":
            count1=count1+1
        else:
            count2=count2+1
    if count1==count2:
        return "Tie"
    elif count1>count2:
        return "Team1"
    else:
        return "Team2"
print(find_winner_of_the_day("Team1","Team2","Team2","Team1","Team2"))
