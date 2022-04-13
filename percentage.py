
aCount = 0
cCount = 0
tCount = 0
gCount = 0
uCount = 0

for char in Seq.upper(): # To converts all lowercase characters in a string into uppercase characters and returns it.
    if char == "A":nt
        aCount = aCount + 1
    elif char == "C":
        cCount = cCount + 1
    elif char == "T":
        tCount = tCount + 1
    elif char == "G":
        gCount = gCount + 1
    elif char == "U":
        uCount = uCount + 1

print ("Percentage of A:", (float(aCount) / len(Seq)) * 100)#Print the A Percentage
print ("Percentage of C:", (float(cCount) / len(Seq)) * 100)#Print the C Percentage
print ("Percentage of T:", (float(tCount) / len(Seq)) * 100)#Print the T Percentage
print ("Percentage of G:", (float(gCount) / len(Seq)) * 100)#Print the G Percentage
print ("Percentage of U:", (float(uCount) / len(Seq)) * 100)#Print the U Percentage
