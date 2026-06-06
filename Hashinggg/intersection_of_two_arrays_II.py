def intersection_of_two_arrays_II(nums1,nums2):
    seen={}
    result=[]
    for num in nums1:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    for number in nums2:
        if number in seen and seen[number]>0:
            result.append(number)
            seen[number]-=1
    return result

print(intersection_of_two_arrays_II([4,9,4,2,4],[1,2,3,4,5,12,3,4,5]))
    