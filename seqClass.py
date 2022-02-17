
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # to indicate that the input is a sequencfe
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") # to indicate that the input is a motif

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
args.seq = args.seq.upper() # if the input sequence is in lower case, we change it to upper case 

if 'U' in args.seq and 'T' in args.seq: # searches for the nucleotides T and U, if both are found in the same sequence it returns a message that it is not DNA or RNA
    print ('The sequence is not DNA nor RNA')
    sys.exit() # if this condition is met, it does not execute any of the "if" after it

if re.search('^[ACGTU]+$', args.seq): # search for ACGTU characters in the sequence args.seq. "+" indicates that they may match one or more times, from the beginning "^" to the end "$" (for line breaks, among others)
    if re.search('T', args.seq): # if it finds T in args.seq, it returns a message it is a DNA seqeunce
        print ('The sequence is DNA')
    elif re.search('U', args.seq): # if it finds U in args.seq, it returns a message it is a RNA sequence
        print ('The sequence is RNA')
    else: # if it does not find T or U it cannot distingunguish, therefore it returns a message that it may be DNAor RNA
        print ('The sequence can be DNA or RNA')
else: # if it does not find the above characters it returns the following message
    print ('The sequence is not DNA nor RNA')

# if the user enters a motif (-m)
if args.motif:
    args.motif = args.motif.upper() # convert sequence to uppercase characters
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '') # returns the message that the motif is being searched for in the sequence
    if re.search(args.motif, args.seq): # if there is a match, print "found" message
        print("FOUND")
    else: # if there is no match of the indicated motif, print "not found"
        print("NOT FOUND")
