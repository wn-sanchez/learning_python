#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = input('Enter file name: ')
fh = open(fname)
counts = dict()

for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != 'From': continue # Skip if no words or doesn't start with 'From'
    sender = words[1] 
    counts[sender] = counts.get(sender, 0) + 1
#print(list(counts.items()))

bigcount = None
bigsender = None
for sender,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigsender = sender
print(bigsender, bigcount)


