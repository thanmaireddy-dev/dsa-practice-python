def boats_to_save_people(people, limit):
    n= len(people)
    people.sort()
    count=0
    p1=0
    p2=n-1
    while (p1<=p2):
        weight= people[p1]+ people[p2]
        if weight> limit:
            count=count+1
            p2=p2-1
        else:
            count=count+1
            p1=p1+1
            p2=p2-1
    return count

print(boats_to_save_people([3,5,3,4],5))