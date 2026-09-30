def rotate(nums, k):
    n=len(nums)
    k=k%n
    def reverse(p1,p2):
        while (p1<p2):
            nums[p1], nums[p2]= nums[p2], nums[p1]
            p1=p1+1
            p2=p2-1
        return nums
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
    return nums

print(rotate([1,2,3,4,5,6,7],3))