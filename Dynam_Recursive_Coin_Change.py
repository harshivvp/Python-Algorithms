def dynam_rec_coin(target,coins,known_results):

    #Default output to the target
    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1

    #return a known result if it's greater than 0
    elif known_results[target] > 0:
        return known_results[target]

    for i in [c for c in coins if c <= target]:

        num_coins = 1 + dynam_rec_coin(target - i,coins,known_results) #target - i = current location of target
        if num_coins < min_coins:
            min_coins = num_coins

            #Resetting the known result
            known_results[target] = min_coins

    return min_coins

target = 23
print(dynam_rec_coin(target,[1,5,10],[0] * (target + 1)))

#For target = 23, output will be 5 because, 10+10+1+1+1 = 5 number counts
