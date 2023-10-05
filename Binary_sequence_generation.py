def generateBinarySequences(n, sequence):
    if n == 0:
        print(sequence)
    else:
        generateBinarySequences(n - 1, sequence + "0")
        generateBinarySequences(n - 1, sequence + "1")

n = int(input())

generateBinarySequences(n, "")