def interval_list_intersection(firstList, secondList):
    n= len(firstList)
    m= len(secondList)
    i=j=0
    result=[]
    while i<n and j<m:
        startA, endA= firstList[i]
        startB, endB= secondList[j]
        
        start= max(startA, startB)
        end= min(endA, endB)
        if start<= end:
            result.append([start, end])
            
        if endA< endB:
            i=i+1
        else:
            j=j+1
    return result 

print(interval_list_intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))