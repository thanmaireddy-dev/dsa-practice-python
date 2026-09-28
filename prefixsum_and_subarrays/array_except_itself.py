def product_of_array_except_itself(nums):
    n= len(nums)
    result=[0]*n
    prefix=[0]*n
    suffix=[0]*n
    prefix[0]= nums[0]
    suffix[n-1]= nums[n-1]
    for i in range(1,n):
        prefix[i]= prefix[i-1]*nums[i]
    for i in range(n-2,-1,-1):
        suffix[i]= suffix[i+1]*nums[i]
    for i in range(n):
        left_prod= prefix[i-1] if i>0 else 1
        right_prod= suffix[i+1] if i<n-1 else 1
        result[i]= left_prod* right_prod
    return result

print(product_of_array_except_itself([-1,1,0,-3,3]))
        