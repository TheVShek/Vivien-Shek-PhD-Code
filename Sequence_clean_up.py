# read in file and splt by entry
f = open("Hpol_transcriptome_SP_HITS.txt")
rawseq = f.read().split(">")[1:]
f.close()

# dictionary for storing the name and sequence
rawseqDict = {}
for sequence in rawseq:
    key = sequence.split("\n")[0]
    seq = "".join(sequence.split("\n")[1:])
    rawseqDict[key] = seq

# matches will be a dictionary with the sequnce as key and  a list of names
matches = {}

# iterate through all the items in the dictionry of sequnces
for name, seq in rawseqDict.items():
    # if sequence is already a key in matches, it means that the sequence has been seen before, so it a duplicate, then add it to the end of a list of names for that particular sequence
    if seq in matches:
        matches[seq].append(name)
    else:
        # if not then just create a new entry in the dictionary
        matches[seq] = [name]

# iterate thought all the sequences again

for seq, names in matches.items():
    if len(names) == 1:
        # print out all the names
        print(">" + names[0])
        # print the sequence
        print(seq)
for seq, names in matches.items():
    # if the length of names is greater than 1, it means that the sequnce appears more than 1 time
    if len(names) > 1:
        # print out all the names
        for n in names:
            print(">" + n)
        # print the sequence
        print(seq)
