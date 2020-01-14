
fname = input("Enter file name: ")
fh = open(fname)

# string -> list 변경
finlist = list()
for line in fh:
    line = line.rstrip()

    #각 line 들 split
    lst = line.split()

    #split 된 항목들을 finlist에 추가
    for word in lst:
        if word not in finlist:
            finlist.append(word)

finlist.sort()
print(finlist)
