def check_if_numbers_are_ascending(s):
    ans=[]
    words= s.split()
    for word in words:
        if word.isdigit():
            ans.append(int(word))
    n= len(ans)
    for i in range(1,n):
        if ans[i]<=ans[i-1]:
            return False
    return True

print(check_if_numbers_are_ascending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))