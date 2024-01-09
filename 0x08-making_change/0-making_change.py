def makeChange(coins, total):
    each_total = [float("inf")] * (total + 1)

    # 0 amount requires 0 coins
    each_total[0] = 0

    # Loop through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            # The fewest number of coins to get total i
            # is minimum of without current coin or with current coin
            each_total[i] = min(each_total[i], each_total[i - coin] + 1)

    # If the total cannot be reached by any number of coins, return -1
    if each_total[total] == float("inf"):
        return -1

    # Return the fewest number of coins needed to get the total
    return each_total[total]
