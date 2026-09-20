def truncateSentence(s, k):
    words= s.split()
    n=len(words)
    for i in range(n-k):   #or can be done with newarr= words[:k]
        words.pop()
    return " ".join(words)

print(truncateSentence("I am a queencard , you wanna be the queencard?", 4))