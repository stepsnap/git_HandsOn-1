aCount = 0
cCount = 0
tCount = 0
gCount = 0
uCount = 0

for char in Seq.upper():
    if char == "A":
        aCount = aCount + 1
    elif char == "C":
        cCount = cCount + 1
    elif char == "T":
        tCount = tCount + 1
    elif char == "G":
        gCount = gCount + 1
    elif char == "U":
        uCount = uCount + 1

print ("Percentage of A:", (float(aCount) / len(Seq)) * 100)
print ("Percentage of C:", (float(cCount) / len(Seq)) * 100)
print ("Percentage of T:", (float(tCount) / len(Seq)) * 100)
print ("Percentage of G:", (float(gCount) / len(Seq)) * 100)
print ("Percentage of U:", (float(uCount) / len(Seq)) * 100)