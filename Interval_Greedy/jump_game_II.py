def jump_game_2(nums):
    n= len(nums)
    jumps=0
    curr_end=0
    farthest=0
    for i in range(n-1):
        farthest= max(farthest, i+nums[i])
        if i==curr_end:
            jumps= jumps+1
            curr_end= farthest
    return jumps 

print(jump_game_2([2,3,1,1,4]))