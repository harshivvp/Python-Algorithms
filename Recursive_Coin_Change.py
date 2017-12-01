def rec_coin(target,coins):

    #Default target value
    min_coins = target

    #Check if target is in coin's value list
    if target in coins:
        return 1

    else:
        # for every coin value that is < = my target val
        for i in [c for c in coins if c <= target]:
            #Add a coin count + recursive call
            num_of_coins = 1 + rec_coin(target - i , coins)
            if num_of_coins < min_coins:
                min_coins = num_of_coins


    return min_coins