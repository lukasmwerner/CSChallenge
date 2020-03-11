n = int(input())

buildings = []

def inArray(num, limit):
    if num < 0:
        return False
    if num >= limit:
        return False

    return True

def solve(b, x, y):
    amount = 0

    if b[y][x] == "I":
        return 0

    if b[y][x] == "*":
        amount += 1
    
    b[y] = b[y][0:x] + "I" + b[y][x + 1:]


    if inArray(x + 1, 10):
        amount += solve(b, x + 1, y)
    if inArray(x - 1, 10):
        amount += solve(b, x - 1, y)
    if inArray(y - 1, 10):
        amount += solve(b, x, y - 1)
    if inArray(y + 1, 10):
        amount += solve(b, x, y + 1)

    return amount

for x in range(n):
    building = []
    for b in range(10):
        building.append(input())

    buildings.append(building)
    if not x == n - 1:
        input()

answers = []

for building in buildings:

    places = 0

    for y in range(10):
        for x in range(10):
            if building[y][x] == "*":
                places += 1



    broken = False
    for y in range(10):
        for x in range(10):
            if building[y][x] == "*":
                connections = solve(building, x, y)
                if connections == places:
                    answers.append("Accept")
                else:
                    answers.append("Reject")
                    broken = True
                    break
        if broken:
            break


for a in answers:
    print(a)
