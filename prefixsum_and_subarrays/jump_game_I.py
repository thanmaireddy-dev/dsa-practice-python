def Jump_Game_I(arr):
    n= len(arr)
    maxreach= 0
    for i in range(n):
        if i>maxreach:
            return False
        maxreach= max(maxreach, i+arr[i])
        if maxreach>=n-1:
            return True
        
    return True

print(Jump_Game_I([2,4,0,0,0,3]))
    