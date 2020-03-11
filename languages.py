n = int(input())


languages = {}

for x in range(n):
    info = input().split(" ")

    languages[info[0]] = [i.lower() for i in info[1:]]


tests = int(input())

okLangs = []
for x in range(tests):
    ins = input()
    ins = ins.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("("," ").replace(")"," ")
    words = ins.split(" ")

    doubleBreak = False
    for word in words:
        for lan in languages.keys():

            #checkWord = word.replace(",","").replace(".","").replace("!","").replace("?","").replace(";","").replace("(","").replace(")","")
            checkWord = word.strip(",.!?:(); ")
            if checkWord.lower() in languages[lan]:
                okLangs.append(lan)
                doubleBreak = True
                break
        if doubleBreak:
            break

for i in okLangs:
    print(i)