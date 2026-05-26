def count_the_number_of_special_characters_I (word):
    n= len(word)
    count=0
    lower= set()
    upper= set()
    for i in range(n):
        if word[i].isupper():
            upper.add(word[i])
        else:
            lower.add(word[i])
            
    for char in upper:
        if char.lower() in lower:
            count= count+1
    return count

print(count_the_number_of_special_characters_I("aaAbcBC"))