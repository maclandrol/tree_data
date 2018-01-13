#!/usr/bin/python
# Convert a sequence format into another
# need the biopython library to work

from Bio import AlignIO
import sys
accepted_format = {'clustal':'clustal', 'fasta':'fasta', 'nexus':'nexus', 'phylipi':'phylip', 'phylips':'phylip-sequential', 'phylip':'phylip-relaxed', 'stockholm':'stockholm' }
if len(sys.argv)<2:
	print("Usage :  seqconvert input inform outform [output]")
else :
	infile = sys.argv[1]
	inform = "fasta"
	outform = "fasta"
	try:
		inform = accepted_format.get(sys.argv[2], 'fasta')
	except:
		inform = 'fasta'
	try:
		outform = accepted_format.get(sys.argv[3], 'fasta')
	except:
		outform = 'fasta'

	if len(sys.argv)>4:
		output = sys.argv[4]
	else:
		output = infile.split('.')[0]+".out"

	AlignIO.convert(infile, inform, output, outform)
	print("File converted from %s to %s"%(inform, outform))