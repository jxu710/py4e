fname = input("please type the file name u wanna open: ")
# if just hit enter, fname will default to clown.txt
if len(fname) < 1:
    fname = "clown.txt"

handle = open(fname)

counts = dict()
for line in handle:
    words = line.rstrip().split()
    for word in words:
        # idiom: retrieve/create/update counter
        counts[word] = counts.get(word, 0) + 1


# to find the most common word
bigword = None
bigcount = None

for word, count in counts.items():
    # print(word, count)
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
