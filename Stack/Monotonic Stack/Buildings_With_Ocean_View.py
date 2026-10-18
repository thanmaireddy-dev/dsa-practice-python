def findBuildings(heights):
    n= len(heights)
    result=[]
    maxheight=0
    for i in range(n-1,-1,-1):
        if heights[i]>maxheight:
            maxheight= heights[i]
            result.append(i)
    return result[::-1]

print(findBuildings([4,2,3,2,1]))