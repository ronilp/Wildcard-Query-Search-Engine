#Wildcard Queries Search Engine

Given a dataset of documents, here is a Permuterm index system for effective document retrieval of wild card queries.

Two programs, for Part 1 and Part 2 are there named in the 2 given folders, 12629part1.py and 12629part2.py
Required files for both parts are also provided.

Both are in python 3 and to run them,

Part 1:
	1. You must have Dataset.txt and Stopwords.txt in your working directory.
	2. Command to run : 
		python 12629part1.py
	3. 2 output files will be generated named InvertedIndex.txt and PermutermIndex.txt

Part 2:
	1. You must have Dataset.txt, InvertedIndex.txt and PermutermIndex.txt in your working directory.
	2. Command to run : 
		python 12629part2.py
	3. On running you will have to enter Query as commandline argument.
	4. 1 output file will be generated named RetrievedDocuments.txt


Explaination :
	
Part 1: Index Construction

	1. First, the stopwords are tokenized with ", " and stored in a list.
	2. Then the dataset is tokenized with " " and the tokens are stored(excluding stopwords) in a dictionary along with the documentID in which they are present.
	3. Then the InvertedIndex is printed in a file.
	4. For Permuterm Index, the rotation algorithm is followed and all the rotated permutations of tokens from the inverted index are stored in a file.

Part 2: Querying

	1. The wild card queries by user can be divided into 5 cases.
		1. X*               -->         X 
		2. *X				-->			X$*
		3. X*Y				-->			Y$X*
		4. X*Y*Z			-->			(Z$X*) and (Y*)
		5. *X* 				-->			can be converted to X* form
	
	2. The 1st 3 cases can be done by prefix matching with the corresponding forms given in RHS.
	3. 4th and 5th are exceptional cases.
	4. 5th can be converted to 1st case.
	5. For case 4,
		Two queries can be taken and their posting lists can be generated. Then a bitwise AND operation on vectors containing their posting lists can be done to obtain the required result.
		The above meintioned two queries (for case X*Y*Z) are (Z$X*) and (Y*)
