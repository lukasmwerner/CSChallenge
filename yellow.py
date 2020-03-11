i = int(input())
equations = []
for x in range(i):
    equations.append(input())

for each in equations:
    thing = each.split("=")
    mathing = thing[0]
    answer = thing[1]
    found = False

    for n in range(10):
        mathtemp = mathing


        for num in range(len(mathing)):
            if mathtemp[num] == "?":
                mathtemp = mathtemp[0:num]+str(n)+mathtemp[num+1:]




        answertemp = answer



        for num in range(len(answer)):
            if answertemp[num] == "?":
                answertemp = answertemp[0:num]+str(n)+answertemp[num+1:]

        answertemp = int(answertemp)


        if ("+" in mathtemp):
            numbers = mathtemp.split("+")

            firstnum = int(numbers[0])
            secondnum = int(numbers[1])

            if (firstnum+secondnum == answertemp):
                print(n)
                found = True
                break
        elif ("*" in mathtemp):
            numbers = mathtemp.split("*")
            
            firstnum = int(numbers[0])
            secondnum = int(numbers[1])

            if (firstnum*secondnum== answertemp):
                print(n)
                found = True
                break

        else:
            neg = mathtemp[1:].find("-")
            numbers = [mathtemp[0:neg+1], mathtemp[neg+2:]]

            
            if (int(numbers[0])-int(numbers[1]) == int(answertemp)):
                print(n)
                found = True
                break
    if not found:
        print("-1")



"""i = int(input())
equations = []
for x in range(i):
    equations.append(input())

for each in equations:
    thing = each.split("=")
    mathing = thing[0]
    answer = thing[1]
    found = False

    for n in range(10):
        mathtemp = mathing


        for num in range(len(mathing)):
            if mathtemp[num] == "?":
                mathtemp = mathtemp[0:num]+str(n)+mathtemp[num+1:]




        answertemp = answer



        for num in range(len(answer)):
            if answertemp[num] == "?":
                answertemp = answertemp[0:num]+str(n)+answertemp[num+1:]

        if ("+" in mathtemp):
            numbers = mathtemp.split("+")


            if (int(numbers[0])+int(numbers[1]) == int(answertemp)):
                print(n)
                found = True
                break
        elif ("*" in mathtemp):
            numbers = mathtemp.split("*")
            if (int(numbers[0])*int(numbers[1]) == int(answertemp)):
                print(n)
                found = True
                break

        else:
            neg = mathtemp[1:].find("-")
            numbers = [mathtemp[0:neg+1], mathtemp[neg+2:]]
            if (int(numbers[0])-int(numbers[1]) == int(answertemp)):
                print(n)
                found = True
                break
    if not found:
        print("-1")
"""