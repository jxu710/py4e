import re

hand = open("mbox-short.txt")

numlist = list()
for lines in hand:
    lines = lines.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence:(.[0-9.]+)", lines)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print("Max:", max(numlist))
