def no_of_strings_that_appear_as_substring(patterns,word):
    count=0
    for pattern in patterns:
        if pattern in word:
            count=count+1
    return count

print(no_of_strings_that_appear_as_substring(["a","b","c"],"aaaaaabbbbb"))