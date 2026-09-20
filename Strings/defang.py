def defang(address):
    fang= "[.]"
    strr=""
    for char in address:
        if char=='.':
            strr= strr+fang
        else:
            strr= strr+char
    return strr

print(defang("255.100.50.0"))
                