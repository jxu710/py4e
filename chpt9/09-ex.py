fname = input("please type the file name u wanna open: ")
handle = open(fname)

for line in handle:
    print(line.rstrip())
