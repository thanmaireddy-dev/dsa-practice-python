def maximum_len_of_longest_substr_wout_repeating_char(str):
    n= len(str)
    charset= set()
    left=0
    maxlen = float('-inf')
    for right in range (n):
        while str[right] in charset:
            charset.remove(str[left])
            left= left+1
        charset.add(str[right])
        maxlen= max(maxlen, right-left+1 )
    return maxlen if maxlen!= float('-inf') else 0

strr= input("enter the string: ")
print(maximum_len_of_longest_substr_wout_repeating_char(strr))


            
            
    
    