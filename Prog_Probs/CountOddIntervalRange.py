def count_odds(low, high):
    return (high - low) // 2 + (high % 2 and low % 2)

    # high - low // 2 means that we take the number of nums in range and halve it since even and odd only alternate


print(count_odds(1, 7))


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:           # If low number is even
            return (high-low+1)//2 # Then add one and return the floor of the division
        return (high-low)//2 + 1   # ELSE return the floor of the division, and add one
