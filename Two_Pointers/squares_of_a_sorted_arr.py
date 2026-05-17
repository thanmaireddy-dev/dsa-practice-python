def squares_of_a_sorted_array(nums):
    n= len(nums)
    p1=0
    p2= n-1
    result= [0]*n
    tobereplaced= n-1
    while (p1<=p2):
        if abs(nums[p1])< abs(nums[p2]):
            result[tobereplaced]= nums[p2]**2
            p2=p2-1
            tobereplaced-=1
        else:
            result[tobereplaced]= nums[p1]**2
            p1=p1+1
            tobereplaced-=1
    return result 

print(squares_of_a_sorted_array([-7,-3,2,3,11]))
            