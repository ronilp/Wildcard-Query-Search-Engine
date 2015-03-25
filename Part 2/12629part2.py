import os

query = input('Enter Query : ')

parts = query.split("*")

if len(parts) == 3:
    case = 4
elif parts[1] == '':
    case = 1
elif parts[0] == '':
    case = 2
elif parts[0] != '' and parts[1] != '':
    case = 3

if case == 4:
    if parts[0] == '':
        case = 1

print("case = ", case)

inverted = {}
with open('InvertedIndex.txt') as f:
    for line in f:
        temp = line.split( )
        val = temp[1].split(",")
        inverted[temp[0]] = val

#print(inverted)        

permuterm = {}
with open('PermutermIndex.txt') as f:
    for line in f:
        temp = line.split( )
        permuterm[temp[0]] = temp[1]
        
#print(permuterm)

def prefix_match(term, prefix):
    term_list = []
    for tk in term.keys():
        if tk.startswith(prefix):
            term_list.append(term[tk])
    return term_list
        
docID = 0

def processQuery(query):    
    term_list = prefix_match(permuterm,query)
    #print(term_list)
    
    docID = []
    for term in term_list:
        docID.append(inverted[term])
    #print(docID)

    temp = []
    for x in docID:
        for y in x:
            temp.append(y)
    #print(temp)        

    temp = [int(x) for x in temp]
    documentID = 0
    outputfile = open("RetrievedDocuments.txt","w")
    path = r"E:\Google Drive\Acads\Slides\3-2\Information Retrieval\Assignments\Lab 1\Part 2\dataset"
    for root, dirs, files in os.walk(path):
        for file in files:
            documentID = documentID + 1
            with open(os.path.join(path, file)) as f:
                for text in f:
                    if documentID in temp:
                        outputfile.write(file + "\n" + text + "\n")
            f.close()
    outputfile.close()
    return 

if case == 1:
    query = parts[0]
elif case == 2:
    query = parts[1] + "$"
elif case == 3:
    query = parts[1] + "$" + parts[0]
elif case == 4:
    queryA = parts[2] + "$" + parts[0]
    queryB = parts[1]

def bitwise_and(A,B):
    return set(A).intersection(B)
    
if case != 4:
    processQuery(query)
elif case == 4:
# queryA Z$X
    term_list = prefix_match(permuterm,queryA)
    #print(term_list)
    
    docID = []
    for term in term_list:
        docID.append(inverted[term])
    #print(docID)

    temp1 = []
    for x in docID:
        for y in x:
            temp1.append(y)
    #print(temp)        

    temp1 = [int(x) for x in temp1]
# queryB Y
    term_list = prefix_match(permuterm,queryB)
    #print(term_list)
    
    docID = []
    for term2 in term_list:
        docID.append(inverted[term2])
    #print(docID)

    temp2 = []
    for x in docID:
        for y in x:
            temp2.append(y)
    #print(temp)        

    temp2 = [int(x) for x in temp2]

    temp = bitwise_and(temp1,temp2)

  #  print(temp1,temp2,temp)    
    documentID = 0
    outputfile = open("RetrievedDocuments.txt","w")
    path = r"E:\Google Drive\Acads\Slides\3-2\Information Retrieval\Assignments\Lab 1\Part 2\dataset"
    for root, dirs, files in os.walk(path):
        for file in files:
            documentID = documentID + 1
            with open(os.path.join(path, file)) as f:
                for text in f:
                    if documentID in temp:
                        outputfile.write(file + "\n" + text + "\n")
            f.close()
    outputfile.close()
