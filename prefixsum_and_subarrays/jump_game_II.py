def Jump_Game_II(arr):
    n= len(arr)
    jumps=0
    currend=0
    farthest=0
    for i in range(n-1):
        farthest= max(farthest, i+arr[i])
        if i==currend:
            jumps= jumps+1
            currend= farthest
    return jumps

print(Jump_Game_II([2,3,0,1,4]))