def sort012(arr):
    n= len(arr)
    count0= count1= count2= 0
    for num in arr:
        if num==0:
            count0+=1
        elif num==1:
            count1+=1
        else:
            count2+=1
    ind=0       
    for i in range(count0):
        arr[ind]= 0
        ind= ind+1
    for j in range(count1):
        arr[ind]=1
        ind= ind+1
    for k in range(count2):
        arr[ind]= 2
        ind= ind+1
        
    return arr
        
print(sort012([1,2,0,2,1,0,0,1,2,1,1,0]))