def total_waviness_of_number_in_range_I(num1, num2):
    waviness=0
    for number in range(num1, num2+1):
        str_num= str(number)
        n= len(str_num)
        for i in range(1,n-1):
            leftneighbour= str_num[i-1]
            currnum= str_num[i]
            rightneighbour= str_num[i+1]
            
            if currnum< leftneighbour and currnum< rightneighbour:
                waviness= waviness+1
            elif currnum> leftneighbour and currnum > rightneighbour:
                waviness= waviness+1
    return waviness

print(total_waviness_of_number_in_range_I(198, 202))