def maximum_product(nums):
    n=len(nums)
    maxprod=float('-inf')
    for i in range(n):
        for j in range(i+1,n):
            product= (nums[i]-1)*(nums[j]-1)
            maxprod= max(maxprod, product)
    return maxprod

print(maximum_product([1,5,4,5]))