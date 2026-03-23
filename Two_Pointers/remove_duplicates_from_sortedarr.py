# nums= [1,1,2,2,3,3,3,5]
# output= [1,2,3,5,_,_,_,_]
def remove_duplicates_from_sorted_array(nums):
    n= len(nums)
    p1=1
    for i in range(1,n):
        if nums[p1-1]!= nums[i]:
            nums[p1]= nums[i]
            p1=p1+1
    return p1

print(remove_duplicates_from_sorted_array([1,1,2,3,3,4,4,6]))
        
        