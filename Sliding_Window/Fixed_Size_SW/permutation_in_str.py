def permutation_in_a_string(s1,s2):
    n= len(s2)
    k= len(s1)
    s1_freq= {}
    s2_freq={}

    if k>n:
        return False

    for char in s1:
        if char in s1_freq:
            s1_freq[char]+=1
        else:
            s1_freq[char]=1
        
    for i in range(k):
        char= s2[i]
        if char in s2_freq:
            s2_freq[char]+=1
        else:
            s2_freq[char]=1
        
    if s1_freq== s2_freq:
        return True

    for i in range(k,n):
        newchar= s2[i]
        oldchar= s2[i-k]
        if newchar in s2_freq:
            s2_freq[newchar]+=1
        else:
            s2_freq[newchar]=1
        s2_freq[oldchar]-=1

        if s2_freq[oldchar]==0:
            del s2_freq[oldchar]
            
        if s2_freq== s1_freq:
            return True

    return False

print(permutation_in_a_string("ab", "eidboaoo"))


"""
sliding window - important problems
🔥 Tier 1 (Revise 2-3 times)

⭐ Longest Substring Without Repeating Characters
⭐ Fruits Into Baskets
⭐ Longest Repeating Character Replacement
⭐ Minimum Size Subarray Sum
⭐ Subarray Product Less Than K

🔥 Tier 2 (Revise at least once)

⭐ Binary Subarrays With Sum
⭐ Count Number of Nice Subarrays
⭐ Longest Substring with At Most K Distinct
⭐ Subarrays with At Most K Distinct Integers

🔥 Tier 3 (Do once, revise lightly)

⭐ Find All Anagrams in a String
⭐ Permutation in String
⭐ Longest Subarray of 1s After Deleting One Element
"""

    