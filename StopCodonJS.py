dna = input("Enter your DNA sequence: ")
framed = int(input("Enter your desired frame for reading: 0 is default: "))

dna = dna.lower()

def Has_Stop_Codon(dna, frame=0+framed):#Remove the +framed if you don't care for the frame
    "This function looks for an in-frame stop codon"
    Stop_Codon_Found = False
    stop_codons = ['tga','tag','taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i + 3]
        if codon in stop_codons:
            Stop_Codon_Found = True

            break
    return Stop_Codon_Found


if (Has_Stop_Codon(dna)):

    print("Your sequence has a stop codon")
else:
    print("Your sequence does not have a stop codon :(")

if (Has_Stop_Codon(dna)): #Provides the location of the stop codon. There's probably a better way of doing this..
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(framed, len(dna), 3):
        codon = dna[i:i + 3]
        if codon in stop_codons:
            print("Your stop codon is located at position: ", (i + 1))
            break
else:
    pass



