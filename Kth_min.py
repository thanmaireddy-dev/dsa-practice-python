def kth_min_max(arr, k):
    if k > len(arr):
        return None

    arr_sorted = sorted(arr)
    kth_min = arr_sorted[k - 1]
    kth_max = arr_sorted[-k]

    return kth_min, kth_max

print(kth_min_max([1,2,3,4,5,6], 3))
