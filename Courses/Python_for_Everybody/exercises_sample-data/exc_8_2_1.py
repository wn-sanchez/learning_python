#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
##You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#Retrieve the day of the week

fname = input('Enter file name: ')
fh = open(fname)

for line in fh:
    line = line.rstrip()
    #print('Line: ', line)
    words = line.split()
    #print('Words: ', words)
    #Guardian
    if len(words) < 3 or words [0] != 'From'  : continue #3 is because the day of the week is the second word
    print(words[2])
    