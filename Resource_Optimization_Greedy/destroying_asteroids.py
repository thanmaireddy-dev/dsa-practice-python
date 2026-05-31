def destroying_asteroids(mass, asteroids):
    n= len(asteroids)
    asteroids.sort()
    currmass= mass
    for i in range(n):
        if currmass>=asteroids[i]:
            currmass= currmass+ asteroids[i]
        else:
            return False
    return True

print(destroying_asteroids(10, [3,9,19,5,21]))