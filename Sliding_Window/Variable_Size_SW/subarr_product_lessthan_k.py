def subarray_product_less_than_k(nums, k):
    n= len(nums)
    count=0
    product=1
    left=0
    for right in range(n):
        product= product * nums[right]
        while product>=k:
            product= product//(nums[left])
            left= left+1
        count= count+ (right-left+1)
    return count

print(subarray_product_less_than_k([10,5,2,6], 100))
        
    