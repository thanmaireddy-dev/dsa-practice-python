def mostWordsFound(sentences):
    maxwords=0
    for sentence in sentences:
        words= sentence.split()
        maxwords= max(maxwords, len(words))
    return maxwords

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))