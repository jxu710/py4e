fname = input("please type the file name u wanna open: ")
# if just hit enter, fname will default to clown.txt
if len(fname) < 1:
    fname = "clown.txt"

handle = open(fname)

counts = dict()
for line in handle:
    words = line.rstrip().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
