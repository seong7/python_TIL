# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
sfline = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    fline = float(line[len('X-DSPAM-Confidence:'):])
    count = count + 1
    sfline = sfline + fline

#print("Done")
asfline = sfline/count
print ('Average spam confidence:', asfline)
