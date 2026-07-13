def rank_transform(arr):
    sortedarr= sorted(set(arr))
    seen={}
    digit=1
    for num in sortedarr:
        seen[num]=digit
        digit= digit+1
    result=[]
    for number in arr:
        result.append(seen[number])
    return result

print(rank_transform([37,12,28,9,100,56,80,5,12]))