def smallest_letter_greater_than_target(letters, target):
    n= len(letters)
    result=letters[0]
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if letters[mid]> target:
            result=letters[mid]
            high=mid-1
        else:
            low=mid+1
    return result

print(smallest_letter_greater_than_target(["c","f","j"], "a"))