def gas_station(gas, cost):
    n= len(gas)
    start=0
    curr_gas=0
    if sum(gas)< sum(cost):
        return -1
    else:
        for i in range(start,n):
            curr_gas= curr_gas+ gas[i]- cost[i]
            print(curr_gas)
            if curr_gas<0:
                curr_gas=0
                start= i+1
    return start if curr_gas>=0 else -1

print(gas_station([2,3,4],[3,4,3])) 
    
    