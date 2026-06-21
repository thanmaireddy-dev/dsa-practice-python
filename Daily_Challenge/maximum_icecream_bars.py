def maximum_icecream_bars(costs,coins):
    n= len(costs)
    costs.sort()
    count=0
    for i in range(n):
        if costs[i]<=coins:
            count=count+1
            coins=coins-costs[i]
    return count

print(maximum_icecream_bars([10,6,8,7,7,8],5))