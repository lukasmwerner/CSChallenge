import math

n = int(input())

words = []

for x in range(n):
    words.append(input().split(" "))

ogWords = words

vowels = ['a', 'e', 'i', 'o', 'u']

for wordList in words:

    maxPoints = 0
    bestWord = ""

    for word in wordList:
        score = 0

        score += math.floor(len(word) / 2)

        ogWord = word
        
        word = word.lower()


        score += word.count("z") * 2
        score += word.count("x") * 3
        score += word.count("q") * 3

        for v in vowels:
            score += word.count(v)

        if score >= maxPoints:
            maxPoints = score
            bestWord = ogWord

    print(bestWord + " - " + str(maxPoints))
    

