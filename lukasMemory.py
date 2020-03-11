stockCount = int(input())
stock = []
for x in range(stockCount):
    info = input().split(",")
    tupleVersion = (info[0], info[1], info[2])
    stock.append(tupleVersion)
stock = sorted(stock, key=lambda a: a[0])
companyNames = []
for i in stock:
    if i[0] not in companyNames:
        companyNames.append(i[0])
companySplit = {}
for data in stock:
    if not data[0] in companySplit.keys():
        companySplit[data[0]] = [data]
    else:
        companySplit[data[0]].append(data)
for key in companySplit.keys():
    li = companySplit[key]
    fixedData = []
    for i in li:

        if "GB" in i[1]:
            ds = int(i[1].strip("GB")) * 1024
        else:
             ds = int(i[1].strip("MB"))
        i = (i[0], ds, i[2])
        fixedData.append(i)

    companySplit[key] = sorted(fixedData, reverse=True)
stock = []
for key in companyNames:
    li = companySplit[key]
    fixedData = []
    for i in li:
        if i[1]%1024 == 0:
            x = (i[0], str(int(i[1]/1024))+"GB", i[2])
        else:
            x = (i[0], str(int(i[1]))+"MB", i[2])
        fixedData.append(x)
    stock.extend(fixedData)
for i in range(len(stock)-1):
    if stock[i][0] == stock[i+1][0] and stock[i][1] == stock[i+1][0]:
        item1 = int(stock[i][0].strip("MHz"))
        item2 = int(stock[i+1][0].strip("MHz"))
        if item2 > item1:
            stock[i], stock[i+1] = stock[i+1], stock[i]
for i in stock:
    print("{} - ({}, {})".format(i[0], i[1], i[2]))