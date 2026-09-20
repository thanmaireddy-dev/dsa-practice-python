def length_of_last(s):
    words= s.strip().split()
    return len(words[-1])

print(length_of_last("red five diamonds in my bag"))