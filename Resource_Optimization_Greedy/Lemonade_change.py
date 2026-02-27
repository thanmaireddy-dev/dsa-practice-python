def lemonade_change(bills):
    n= len(bills)
    five=0
    ten=0
    for i in range(n):
        if bills[i]==5:
            five= five+5
        elif bills[i]== 10:
            ten= ten+10
            if five>=5:
                five= five-5
            else:
                return False
            
        elif bills[i]== 20:
            if five>=5 and ten>=10:
                ten= ten-10
                five= five-5
            elif five>=15:
                five= five-15
            else:
                return False
            
    return True


print(lemonade_change([5,5,10,10,20]))
    
    