def two_sum_hashmap(arr, target):
    n= len(arr)
    seen= { }
    for i, num in enumerate (arr):
        complement= target- num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

arrr= list(map(int, input("enter the array: ").split()))
t= int(input("enter the target number: "))
print(two_sum_hashmap(arrr, t))