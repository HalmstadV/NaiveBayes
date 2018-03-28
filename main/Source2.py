filename = "dictionary.txt"
f = open(filename, "r+")
for i in range(8222):
    line = f.readline()
    print(line)