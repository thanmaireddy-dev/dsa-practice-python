def basic_calculator_two(s):
    stack=[]
    num=0
    prevop='+'
    for char in s:
        if char.isdigit():
            num= num*10+ int(char)
        elif char==' ':
            continue
        else:
            if prevop=='+':
                stack.append(num)
            elif prevop=='-':
                stack.append(-num)
            elif prevop=='*':
                stack.append(stack.pop()*num)
            else:
                stack.append(int(float(stack.pop())/float(num)))
            prevop= char
            num=0
    if prevop=='+':
        stack.append(num)
    elif prevop=='-':
        stack.append(-num)
    elif prevop=='*':
        stack.append(stack.pop()*num)
    else:
        stack.append(int(float(stack.pop())/float(num)))
    return sum(stack)

print(basic_calculator_two("3+2*2"))