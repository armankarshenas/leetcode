import numpy as np
from collections import defaultdict
def Total_profit(prices):
    map_stock = defaultdict(int)
    map_stock.setdefault('buy', [])
    map_stock.setdefault('sell', [])
    map_stock.setdefault('hold', [])
    if len(prices) > 2:
        if prices[1] > prices[0] and prices[0] < max(prices):
            map_stock["buy"].append(0)
        for i in range(1, len(prices) - 1):
            if prices[i - 1] >= prices[i] and prices[i + 1] > prices[i]:
                map_stock["buy"].append(i)
            elif prices[i - 1] < prices[i] and prices[i + 1] <= prices[i]:
                map_stock["sell"].append(i)
            else:
                map_stock["hold"].append(i)
        if prices[len(prices) - 1] > prices[len(prices) - 2]:
            map_stock["sell"].append(len(prices) - 1)
        print(map_stock)
        total_purchased = sum([prices[k] for k in map_stock['buy']])
        total_sold = sum([prices[k] for k in map_stock['sell']])
        total_profit = total_sold - total_purchased
        return total_profit
    elif len(prices) > 1:
        if prices[1] > prices[0]:
            return prices[1] - prices[0]
        else:
            return 0
    else:
        return 0
prices = [7,1,5,3,6,4]
print(Total_profit(prices))
