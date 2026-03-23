def squares_of_a_sorted_array(nums):
    n= len(nums)
    p1=0
    p2=n-1
    result=[0]*n
    tobereplaced = n-1
    while (p1<=p2):
        if abs(nums[p1])< abs(nums[p2]):
            result[tobereplaced]= nums[p2]
            tobereplaced-=1
            p2=p2-1
        else:
            result[tobereplaced]= nums[p1]
            tobereplaced-=1
            p1=p1+1
    result1=[]
    for num in result:
        result1.append(num**2)
    return result1

print(squares_of_a_sorted_array( [-4,-1,0,3,10]))