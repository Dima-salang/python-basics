"""A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally
optimal choice at each stage with the hope of finding a global optimum. In other words, a greedy algorithm chooses
the best possible option at each step, without considering the consequences of that choice on future steps.

"""


def coin_exchange(amount, coins):
    coins.sort(reverse=True)

    # var to keep track of number of coins
    num_of_coins = 0

    for coin in coins:
        if coin <= amount:
            num_of_coins += amount // coin
            amount %= coin

        if amount == 0:
            break

    return num_of_coins


print(coin_exchange(50, [3, 5, 1, 10]))

