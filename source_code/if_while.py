x = input ("which number?")
if float(x)<10:
    while float(x)>3:
        print(x)
        x=float(x)-1
    print(float(x), "used both if and while")
if int(x)>10: print(x, "is larger than 10")
