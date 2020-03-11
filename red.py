import math
segments = []
for i in range(5):
    segments.append(input().split(" "))
miles = 0
hours = 0
for seg in segments:
    miles += int(seg[0]) / 5280
    hours += int(seg[1]) / 60
avgSpeed = miles/hours
strSpeed = str(round(avgSpeed, 3))
print("Your speed was " + strSpeed +" miles per hour.")