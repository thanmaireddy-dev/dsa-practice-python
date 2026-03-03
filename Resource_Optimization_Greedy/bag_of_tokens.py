def bag_of_tokens(tokens, power):
    n= len(tokens)
    tokens.sort()
    score=0
    max_score=0
    p1=0
    p2= n-1
    while (p1<=p2):
        if tokens[p1]<= power:
            power= power-tokens[p1]
            score= score+1
            p1= p1+1
        elif tokens[p1]>power and score>=1:
            power= power+tokens[p2]
            score= score-1
            p2= p2-1
        else:
            break
        max_score= max(max_score, score)
    return max_score

print(bag_of_tokens([100], 50))