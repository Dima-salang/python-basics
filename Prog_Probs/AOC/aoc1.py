def aoc1(aoc_file):
    result = 0
    with open(aoc_file, "r") as file:
        for code in file:
            res = "".join([char for char in code if char.isdigit()])
            twoDigits = f"{res[0]}{res[-1]}"
            result += int(twoDigits)
    return result


print(aoc1("Prog_Probs\AOC\\aoc1.txt"))
