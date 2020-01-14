def computepay(h,r):
    p = h * r
    ovt_r = r*1.5
    if h>40 : p = (40*r) + (h - 40)*ovt_r
    print(p)
    return

h = float(input("Enter hours: "))
r = float(input("Enter rate: "))
computepay(h,r)
