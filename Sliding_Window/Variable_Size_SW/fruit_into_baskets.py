def fruit_into_basket(fruits):
    n= len(fruits)
    fruit_count={}
    maxlen=0
    p1=0
    p2=0
    for p1 in range(n):
        while len(fruit_count)>2:
            fruit_count[fruits[p2]]-=1
            if fruit_count[fruits[p2]]==0:
                del fruit_count[fruits[p2]]
            p2= p2+1
            
        if fruits[p1] in fruit_count:
            fruit_count[fruits[p1]]+=1
        else:
            fruit_count[fruits[p1]]=1
        maxlen= max(maxlen, p1-p2+1)
    return maxlen

print(fruit_into_basket([0,1,2,2])) 
    
    
    
    