def jump_game_I (arr):
    n= len(arr)
    maxreach=0
    for i in range(n):
        if i>maxreach:
            return False
        maxreach= max(maxreach, i+ arr[i])
        if maxreach>=n-1:
            return True
        
    return True


print(jump_game_I([2,3,1,1,4]))       