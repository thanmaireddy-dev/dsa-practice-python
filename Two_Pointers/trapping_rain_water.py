def trapping_rain_water(heights):
    n= len(heights)
    water=0
    left=0
    right=n-1
    lmax=0
    rmax=0
    while (left< right):
        lmax= max(lmax, heights[left])
        rmax= max(rmax, heights[right])
        if lmax< rmax:
            water= water+ (lmax- heights[left])
            left= left+1
        else:
            water= water+ (rmax- heights[right])
            right= right-1
    return water

print(trapping_rain_water([4,2,0,3,2,5]))
            
        
        