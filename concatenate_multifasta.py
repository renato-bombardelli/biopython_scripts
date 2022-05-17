#!/usr/bin/python3

#Usage to use this script, just change the variables "directory",
# to the path to the directory where your fastA files are located
# Then the "out" with the prefix for the output file

import os
from Bio import SeqIO

directory = "./"
out = "testesin"

output = open(f"{out}.fasta","w")

files = os.listdir(f'{directory}')

for i in files:
    if i != out+".fasta":
        try:
            with open(f'{directory}'+i,"r") as set1:
                for record in SeqIO.parse(set1, "fasta"):
                     SeqIO.write([record], output, "fasta")
        except IsADirectoryError:
            continue
