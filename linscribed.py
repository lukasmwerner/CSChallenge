n = int(input())

alph = ["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','Q','X','Y','Z']

boxes = []

for x in range(n):

    box = []

    length = int(input())

    for y in range(length):
        box.append([])
    
        for i in range(length):
            box[y].append(".")
    boxes.append(box)


    letter = int((length - 1)/2)

    for i in range(letter+1):
        for x in range(length-(i*2)):
            for y in range(length-(i*2)):
                box[x+i][y+i] = alph[letter-i]



c = 0
for box in boxes:
    c += 1
    for x in box:
        for y in x:
            print(y, end="")
        print()
    if c < len(boxes):
        print()
        


    