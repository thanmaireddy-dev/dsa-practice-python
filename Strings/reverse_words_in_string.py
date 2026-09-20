def reverseWords(s):
    words= s.strip().split()
    words.reverse()
    return " ".join(words)

print(reverseWords(" the sky is blue    "))