nums=[1,12,-5,-6,50,3]
maxsum= float('-inf')
k=4
left=0
print("start")
n= len(nums)
winsum= sum(nums[:k])
print(winsum)
maxsum=max(maxsum,winsum)
print(maxsum)

for i in range(k,n):
    winsum= winsum+ nums[i]-nums[left]
    left= left+1
    maxsum= max(maxsum, winsum)
    
print(float(maxsum/k))