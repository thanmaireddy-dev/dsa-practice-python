def container_with_most_water(heights):
    n= len(heights)
    p1=0
    p2=n-1
    maxwater=0
    while (p1<p2):
        currwater= (p2-p1) * min(heights[p1], heights[p2])
        maxwater= max(maxwater, currwater)
        if heights[p1]< heights[p2]:
            p1=p1+1
        else:
            p2=p2-1
    return maxwater


print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
        