def determine_if_two_strings_are_close(word1, word2):
    seen1={}
    seen2={}
    word1_values=[]
    word2_values=[]
    if len(word1)!= len(word2):
        return False
    if set(word1)!= set(word2):
        return False
    for char1, char2 in zip(word1, word2):
        if char1 in seen1:
            seen1[char1]+=1
        else:
            seen1[char1]=1
        if char2 in seen2:
            seen2[char2]+=1
        else:
            seen2[char2]=1
        
    for val in seen1.values():
        word1_values.append(val)
    for val in seen2.values():
        word2_values.append(val)
    word1_values.sort()
    word2_values.sort()
    if word1_values!= word2_values:
        return False
    return True
    
print(determine_if_two_strings_are_close("cabbba", "abbccc"))
    