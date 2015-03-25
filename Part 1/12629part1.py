import os

with open('Stopwords.txt') as f:
    for line in f:
        stopwords = line.split(", ")
#print stopwords

tokens = {}
documentID = 0
path = r"E:\Part 1\dataset"

for root, dirs, files in os.walk(path):
    for file in files:
        with open(os.path.join(path, file)) as f:
                documentID += 1
                line_tokens = []
                for line in f:
                    line_tokens = line.split(  )
                    for each in line_tokens:
                        if each not in stopwords:
                            if each not in tokens:
                                tokens[each] = [documentID]
                            else:
                                tokens[each].append(documentID)

file = open("InvertedIndex.txt", "w")
for key in sorted(tokens):
    file.write(key)
    file.write(" ")
    value = ','.join(str(v) for v in tokens[key])
    file.write(value)
    file.write("\n")
file.close()

def rotate(str, n):
    return str[n:] + str[:n]

file = open("PermutermIndex.txt","w")
keys = tokens.keys()
for key in sorted(keys):
    dkey = key + "$"
    for i in range(len(dkey),0,-1):
        out = rotate(dkey,i)
        file.write(out)
        file.write(" ")
        file.write(key)
        file.write("\n")
file.close()
