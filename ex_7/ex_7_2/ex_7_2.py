# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
# counting lines and finding total
total = 0
count = 0
for num in fh:
    if not num.startswith("X-DSPAM-Confidence:") :
        continue
    atpos = num.find('0')

    val = num[atpos:]
    total = total + float(val)
    count = count +1

print("Average spam confidence:",total/count)
