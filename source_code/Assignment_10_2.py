x =  input('Enter a file name: ')
if len(x) == 0: x = "mbox-short.txt"
hand = open(x,'r')

#원하는 data 추출하여 dictionary 작성
hr = dict()
for line in hand :
    if line.startswith('From '):
        spc = line.split()
        cln = spc[5].split(':')
        hr[cln[0]] = hr.get(cln[0],0) + 1

#dictionary를 list로 전환 및 원하는대로 sort
slst = sorted(hr.items())
for h,c in slst :
    print (h,c)
