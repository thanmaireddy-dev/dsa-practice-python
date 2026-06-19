def find_the_highest_altitude(gain):
    n= len(gain)
    prefixsum=[0]*(n+1)
    for i in range(n):
        prefixsum[i+1]= prefixsum[i] + gain[i]
    return max(prefixsum)

print(find_the_highest_altitude([-4,-3,-2,-1,4,3,2]))