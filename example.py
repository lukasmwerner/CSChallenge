import sys
try:
    loopi = int(input())
except Exception as e:
    sys.exit()    
    
words = []

for x in range(loopi):
    b = input()
    words.append(b)
    
for word in words:
    print("I like " + word+".")

    