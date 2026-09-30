def rotateString(s, goal):
    if len(goal)<len(s):
        return False
    s= s+s
    return goal in s

print(rotateString("abcde", "cdeab"))