# print out from mbox-short.txt hour in ascending order & its count
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
di = dict()
#find 'From', split by ' '
for line in handle:
    word = line.rstrip('\n').split(' ')
    #extract sender line and get time
    if word[0] != 'From' :
        continue
    time = word[6:7]
    #split by ':' and get hour
    for t in time:
        t = t.split(':')
        hour = t[0:1]
    #create dict k,v of (time,count)
    for hr in hour :
        di[hr] = di.get(hr,0) + 1
#sort in ascending order (horizontal list)
h = sorted(di.items())
#print vertical list
for k,v in h:
    print(k,v)
