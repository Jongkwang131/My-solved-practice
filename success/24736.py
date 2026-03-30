visiting_goals = list(map(int, input().split()))
home_goals = list(map(int, input().split()))

visiting_scores = visiting_goals[0]*6 + visiting_goals[1]*3 + visiting_goals[2]*2 + visiting_goals[3]*1 + visiting_goals[4]*2
home_scores = home_goals[0]*6 + home_goals[1]*3 + home_goals[2]*2 + home_goals[3]*1 + home_goals[4]*2


print(visiting_scores, home_scores)