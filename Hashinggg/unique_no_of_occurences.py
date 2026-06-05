def unique_number_of_occurences(arr):
    n= len(arr)
    seen={}
    result=[]
    for num in arr:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    for val in seen.values():
        result.append(val)
    return len(result)== len(set(result))

print(unique_number_of_occurences([1,1,2,2,2,3,3]))
            