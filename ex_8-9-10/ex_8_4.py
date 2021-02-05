#open romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
collection = list()
# stripping newline & splitting
for str in fh:
    line = str.rstrip('\n')
    lst = line.split(' ')
    #divide to individual words and loop
    for word in lst:
        #ensure no duplicate words
        if word not in collection:
            collection.append(word)
        else:
            continue
#sort alphabetically
collection.sort()
print(collection)

#shorter alt, on line 6 add: .split(' ') and get rid of line 7
#example code:
#for str in fh:
    #line = str.rstrip('\n').split(' ')
    #note: divide to individual words and loop
    #for word in line:
        #note: ensure no duplicate words
        #if word not in collection:
            #collection.append(word)
        #else:
            #continue
