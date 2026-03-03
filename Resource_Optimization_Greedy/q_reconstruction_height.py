def queue_reconstruction_by_height(people):
    people.sort(key=lambda x: (-x[0], x[1]))
    result=[]
    for person in people:
        result.insert(person[1], person)
    return result 

print(queue_reconstruction_by_height([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))