""" NOTE TO MYSELF:
I NEED TO WORK ON RECURSIVE PROBLEMS. I AM EVEN HAVING PROBLEMS WITH SUCH AN EASY PROBLEM.
"""


def numberOfMatches(n):
    print(playMatchRecursive(7))
    print(playMatchIterative(7))

def playMatchRecursive(teams, numofMatches=0):
    if teams <= 1:
        return numofMatches
    
    if teams % 2 == 0:
        print("Number of teams:", teams)
        numofMatches += teams // 2
        teams //= 2
        print("Teams advanced: ", teams)
        print("Number of matches: ", numofMatches)
    else:
        print("Number of teams: ", teams)
        numofMatches += (teams - 1) // 2
        teams = (teams - 1) // 2 + 1
        print("Teams advanced: ", teams)
        print("Number of matches: ", numofMatches)

    return playMatchRecursive(teams, numofMatches)
    

def playMatchIterative(teams):
    numofMatches = 0
    while teams > 1:
        if teams % 2 == 0:
            print("Number of teams:", teams)
            numofMatches += teams // 2
            teams //= 2
            print("Teams advanced: ", teams)
            print("Number of matches: ", numofMatches)
        else:
            print("Number of teams: ", teams)
            numofMatches += (teams-1) // 2
            teams = (teams-1)//2+1
            print("Teams advanced: ", teams)
            print("Number of matches: ", numofMatches)

    return numofMatches


numberOfMatches(n=10)
        
        
