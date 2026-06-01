def minimum_cost_of_buying_candies_with_discount(cost):
    n= len(cost)
    if n<=2:
        return sum(cost)
    cost.sort()
    summ=0
    p1=n-1
    p2=n-2
    while (p2>=0):
        summ= summ+ cost[p1]+ cost[p2]
        p1=p1-3
        p2=p2-3
    while (p1>=0):
        summ= summ+ cost[p1]
        p1=p1-3
    return summ

print(minimum_cost_of_buying_candies_with_discount([6,5,7,9,2,2]))
    