# open mbox-short.txt
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
count = dict()
#search 'From' and create dictionary of emails
for line in handle:
    word = line.rstrip('\n').split(' ')
    #extract sender line and emails
    if word[0] != 'From' :
        continue
    email = word[1:2]
    #make dictionary of emails
    for mailer in email :
        count[mailer] = count.get(mailer, 0) + 1
#count most frequent emailer
topcount = None
topmailer = None
for mailer,num in count.items() :
    if topcount is None or num > topcount:
        topmailer = mailer
        topcount = num

print(topmailer,topcount)
