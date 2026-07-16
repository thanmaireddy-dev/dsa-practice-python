import math
def sum_of_gcd_of_formed_pairs(nums):
    maxnums=[]
    prefixgcd=[]
    currmax=0
    for num in nums:
        currmax= max(currmax,num)
        maxnums.append(currmax)
    for num1, num2 in zip(maxnums,nums):
        prefixgcd.append(math.gcd(num1, num2))
    prefixgcd.sort()
    n=len(prefixgcd)
    p1=0
    p2=n-1
    totalsum=0
    while (p1<p2):
        totalsum= totalsum+ math.gcd(prefixgcd[p1], prefixgcd[p2])
        p1=p1+1
        p2=p2-1
    return totalsum

print(sum_of_gcd_of_formed_pairs([3,6,2,8]))
        