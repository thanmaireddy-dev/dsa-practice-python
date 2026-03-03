def best_time_to_buy_and_sell_stock_II(prices):
    n= len(prices)
    profit=0
    max_profit= 0
    for i in range(n-1):
        if prices[i+1]> prices[i]:
            profit= profit+ (prices[i+1]- prices[i])
            max_profit= max(max_profit, profit)
    return max_profit

print(best_time_to_buy_and_sell_stock_II([7,1,5,3,6,4]))
    