#!/usr/bin/python3

# Description: Fix fasta files that are truncated with different lines length of the sequences

from Bio import SeqIO
import sys

output = open(sys.argv[1]+".fix.fas","w")
with open(sys.argv[1],"r") as set1:
    for i in SeqIO.parse(set1,"fasta"):
        header = i.id
        seq = i.seq
        output.write(">"+str(header)+"\n"+str(seq)+"\n")
