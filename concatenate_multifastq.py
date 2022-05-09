#!/usr/bin/python3

#Usage to use this script, just change the variables "directory",
# to the path to the directory where your fastq files are located
# Then the "out" with the prefix for the output file

import os
from Bio import SeqIO

directory = "./pass"
out = "multifastq_nema_ssci_ont"

output = open(f"{out}.fastq","w")

files = os.listdir(f'{directory}')

for i in files:
	with open(f'{directory}'+i,"r") as set1:
	    for record in SeqIO.parse(set1, "fastq"):
	    	 SeqIO.write([record], output, "fastq")
