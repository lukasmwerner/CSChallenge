n = int(input())
items = []
for x in range(n):
    info = input().split(",")
    newTuple = (info[0], info[1], info[2])
    items.append(newTuple)
nameSorted = sorted(items, key=lambda a: a[0])
companies = {}
names = []
for item in nameSorted:
    if item[0] not in names:
        names.append(item[0])
    if item[0] not in companies:
        companies[item[0]] = []
    companies[item[0]].append((item[1], item[2]))
ramSorted = []
for comp in companies.keys():
    data = companies[comp]
    saveState = []
    for d in data:
        old = d
        newMem = 0
        mem = d[0]
        print(mem[-2:])
        if(mem[-2:] == "GB"):
            newMem = int(mem[0:-2]) * 1024
        else:
            newMem = int(mem[0:-2])
        d = (newMem, int(d[1][0:-3]))
        saveState.append((newMem, d))
    companies[comp] = sorted(data, key=lambda a: a[0], reverse=False)
    for d in data:
        correctItem = ""
        newTuple = (comp,correctItem,)
        ramSorted.append(newTuple)
print(ramSorted)