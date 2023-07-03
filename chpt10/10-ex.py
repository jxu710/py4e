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

#to make dictionary into list of tuples

# 一种解法

temp = list()
x = sorted(counts.items(),reverse=True)
for (k,v) in x:
    newt=(v,k)
    temp.append(newt)

for (v,k) in temp[:5]:
    print(k,v)


# 另一种解法
# print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )


