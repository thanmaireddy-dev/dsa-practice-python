def best_time_to_buy_and_sell_stock_I(prices):
    n= len(prices)
    buy= prices[0]
    profit=0
    max_profit=0
    for i in range(1,n):
        if prices[i]< buy:
            buy= prices[i]
        else:
            profit= prices[i]- buy
            max_profit= max(max_profit, profit)
    return max_profit

print(best_time_to_buy_and_sell_stock_I([7,1,5,3,6,4]))
    
    