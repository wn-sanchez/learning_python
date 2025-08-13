#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = input('Enter file name: ')

# If the user just hits Enter (empty input), it defaults to "mbox-short.txt"
if len(fname) < 1: fname = "mbox-short.txt"

fh = open(fname)
counts = dict()

for line in fh:
    line = line.rstrip() 
    words = line.split()
    
    # Skip if no words or doesn't start with 'From'. 6 is because hour is in position 5
    if len(words) < 6 or words[0] != 'From': 
        continue
    
    # Extract hour from time (words[5] contains the time like "09:14:16")
    time_str = words[5]  # This is the time portion
    hour = time_str.split(':')[0]  # Get just the hour
    
    # Count occurrences of each hour
    counts[hour] = counts.get(hour, 0) + 1

# Convert dictionary to list of tuples (value, key) for sorting
newlist = list()
for key, val in counts.items():
    tup = (key,val)
    newlist.append(tup)

# sort by key (hour)
hour_sorted = sorted(newlist)
for hour, count in hour_sorted:
    print(hour, count)

        



    
    
    