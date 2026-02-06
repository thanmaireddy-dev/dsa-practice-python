def gas_station(gas, cost):
    n= len(gas)
    currgas=0
    start=0
    if sum(gas)<sum(cost):
        return -1
    else:
        for i in range(start, n):
            currgas= currgas+ gas[i] - cost[i]
            if currgas<0:
                currgas=0
                start= i+1
    return start

print(gas_station([2,3,4],[3,4,3]))