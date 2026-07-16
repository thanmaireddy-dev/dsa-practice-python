#3754. Concatenate Non-Zero Digits and Multiply by Sum I
def concatenate_digits(number):
    non_zero_digits=[]
    strnum= str(number)
    for digit in strnum:
        if digit!='0':
            non_zero_digits.append(digit)
    if not non_zero_digits:
        return 0
    x=int("".join(non_zero_digits))
    summ=0
    for digit in non_zero_digits:
        summ= summ+ int(digit)
    return x*summ

print(concatenate_digits(10203004))
    