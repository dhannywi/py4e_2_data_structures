#open mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
#find lines, strip and split
for line in fh:
    email = line.rstrip('\n').split(' ')
    #extract email
    if email[0] != 'From' :
        continue
    print(email[1])
    #count email address
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
