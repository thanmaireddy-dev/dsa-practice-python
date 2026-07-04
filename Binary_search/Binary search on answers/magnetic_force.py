#lc 1552 - Magnetic Force Between Two Balls - same as Aggresive Cows
def magnetic_force(position,m):
    n=len(position)
    position.sort()
    def can_place(mid, position, m):
        balls=1
        lastposition=position[0]
        for i in range(1,n):
            if (position[i]-lastposition)>=mid:
                balls=balls+1
                lastposition= position[i]
        if balls>=m:
            return True
        else:
            return False
        
    low=1
    high=max(position)- min(position)
    while (low<=high):
        mid=(low+high)//2
        if can_place(mid, position, m):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result

print(magnetic_force( [1,2,3,4,7],3))
        
                
                