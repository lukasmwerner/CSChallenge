n = int(input())

words = []


def vowelsFound(word):
    count = 0
    for char in word:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count +=1
    return count

for x in range(n):
    words.append(input().split(" "))

for line in words:
    scores = []
    for word in line:
        ogWord = word
        word = word.lower()
        score = int(len(word)/2) + 1*vowelsFound(word) + 2*word.count("z") + 3*word.count("x") + 3*word.count("q")
        scores.append(
            (ogWord, score)
        )
    bestFirst = sorted(scores, key=lambda a: a[1], reverse=True)
    bestWord = bestFirst[0]
    print(bestWord[0] + " - " + str(bestWord[1]))
