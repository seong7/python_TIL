file = input('Enter the file name:')
if len(file)  == 0 : file = 'mbox-short.txt'
handle = open(file)

sender = dict()
for line in handle :
    if line.startswith('From ') :
        emails = line.split()
        # idion : retrieve/create/update counter
        sender[emails[1]] = sender.get(emails[1],0) +1

bigcount = None
bigsender = None
for key,count in sender.items() :
    if count > bigcount :
        bigcount = count
        bigsender = key
print (bigsender, bigcount)
