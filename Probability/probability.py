import random

dice = [1, 2, 3, 4, 5, 6]

def main():
    NUM_TRIALS = 1_000_000
    TARGET_SUM = 7
    n_event = 0
    for i in range(NUM_TRIALS):
        roll_sum = sum_rolls()
        print(f"Trial {i}")
        if roll_sum == TARGET_SUM:
            n_event += 1
    pr_e = n_event/NUM_TRIALS
    print(f"Probability of event summing to {TARGET_SUM}: {pr_e}")

def sum_rolls():
    roll_1 = roll_dice()
    roll_2 = roll_dice()
    return roll_1 + roll_2
 
def roll_dice():
    return random.choice(dice)
    


if __name__ == '__main__':
    main()