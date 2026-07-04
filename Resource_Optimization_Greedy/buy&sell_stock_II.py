def best_time_to_buy_and_sell_stock_II(prices):
    n= len(prices)
    profit=0
    for i in range(1,n):
        if prices[i]> prices[i-1]:
            profit= profit+ (prices[i]-prices[i-1])
    return profit

print(best_time_to_buy_and_sell_stock_II([1,2,3,4,5]))
    