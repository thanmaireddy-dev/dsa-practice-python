def find_gcd_of_array(nums):
    n=len(nums)
    minimum=nums[0]
    maximum=nums[0]
    for i in range(1,n):
        if nums[i]<minimum:
            minimum= nums[i]
        if nums[i]>maximum:
            maximum=nums[i]
    def find_gcd(a,b):
        if b==0:
            return a
        else:
            return find_gcd(b,a%b)
    return find_gcd(minimum, maximum)

print(find_gcd_of_array([7,5,6,8,3]))