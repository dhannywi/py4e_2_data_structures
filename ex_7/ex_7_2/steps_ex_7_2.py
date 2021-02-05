#finding and printing spam input (and stripped newline)
fname = input("Enter file name: ")
fh = open(fname)
# find lines
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    print(line.rstrip())
# works

# isolating counting lines
fname = input("Enter file name: ")
fh = open(fname)
# find lines
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
print(count)
# works

#finding float position
fname = input("Enter file name: ")
fh = open(fname)
# find lines
for num in fh:
    if not num.startswith("X-DSPAM-Confidence:") :
        continue
    atpos = num.find('0')
    print(atpos)
# works

# find float values
fname = input("Enter file name: ")
fh = open(fname)
# find lines
for num in fh:
    if not num.startswith("X-DSPAM-Confidence:") :
        continue
    atpos = num.find('0')

    val = num[atpos:]
    print(float(val))
# works

#finding total
fname = input("Enter file name: ")
fh = open(fname)
# find lines
total = 0
for num in fh:
    if not num.startswith("X-DSPAM-Confidence:") :
        continue
    atpos = num.find('0')

    val = num[atpos:]
    total = total + float(val)
print(total)
# works!

# counting lines and finding total together (finally!!!)
# fuck! turns out I gotta condense my code or else it calculates the wrong values
total = 0
count = 0
for num in fh:
    if not num.startswith("X-DSPAM-Confidence:") :
        continue
    atpos = num.find('0')

    val = num[atpos:]
    total = total + float(val)
    count = count +1
print(total)
print(count)
# works!!! (see final code in ex_7_2.py)
