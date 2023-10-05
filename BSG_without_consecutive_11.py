def generateBinarySequences(n, sequence):
    if len(sequence) == n:
        print(sequence)
    else:
        if len(sequence) >= 1 and sequence[-1] == "1":
            generateBinarySequences(n, sequence + "0")
        else:
            generateBinarySequences(n, sequence + "0")
            generateBinarySequences(n, sequence + "1")

n = int(input())

generateBinarySequences(n, "")