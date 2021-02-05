# Use words.txt as the file name
# change characters to uppercase
fname = input("Enter file name: ")
fh = open(fname)

for li in fh :
    ls = li.rstrip()
    print(ls.upper())
