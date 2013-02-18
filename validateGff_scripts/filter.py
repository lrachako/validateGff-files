## gff3_filter.py 
## Created by: Rachakonda.L.Sowmya
## This script takes in a gff3 file and checks for and fixes the following:
## 1. Presence of "##gff-version 3" line
## 2. Filters out all the non protein-coding features from the gff3 file
## Usage : python gff3_filter your_gff3file >your_output_file

#!usr/bin/python

import sys
import re

IDS=[]
inFile=open(sys.argv[1],"r") # Input gff3 file
f1=inFile.readlines() 
outFile1=open(sys.argv[2],"w")
outFile2=open(sys.argv[3],"w")
outFile1.write("##gff-version 3\n")
outFile2.write("##gff-version 3\n")
commentline="###Gene"
features=['gene','mRNA','CDS']
mydict={}
# First pass
for line in f1:
	line=line.rstrip("\n")
	if line.strip():
		if line==commentline:
			IDS.append(mydict)
			mydict={}
		elif line[0][0]=="#":
			continue
		else:
			cols=line.strip().split('\t') #Split the line into columns and store it in an array
			desc=cols[8] # Takes the 9th column of the input gff3 file
			feature=cols[2] # Takes the second column of the input gff3 file
			mydesc=desc.split(';') # Split the 9th column into individual fields
			for item in mydesc:
				if "ID=" in item:
					id=item.split('=')
					if feature in features:
						mydict[id[1]]=feature	
IDS.append(mydict)

Protein_IDS=[]

for dict in IDS:
	keys=dict.keys()
	count=0
	while count<len(dict):
		for key in keys:
			if key in features:
				count=count+1
	if count==len(dict):
		Protein_IDS.append(dict.values())
	else:
		Protein_IDS.append([])

# Second pass
index=0
for line in f1:
	line=line.rstrip("\n")
	if line.strip():
		if line==commentline:
			index+=1
		elif line[0][0]=="#":
			continue
		else:
			cols=line.strip().split('\t') #Split the line into columns and store it in an array
                        desc=cols[8] # Takes the 9th column of the input gff3 file
                        feature=cols[2] # Takes the second column of the input gff3 file
                        mydesc=desc.split(';') # Split the 9th column into individual fields
                        for item in mydesc:
                                if "ID=" in item:
                                        id=item.split('=')
					if id[1] in Protein_IDS[index]:
						outFile1.write(line)
						outFile1.write("\n")
						break
					else:
						outFile2.write(line)
						outFile2.write("\n")
						break
				elif "Parent=" in item:
					id =item.split('=')
					if id[1] in Protein_IDS[index]:
						outFile1.write(line)
						outFile1.write("\n")
						break
					else:
						outFile2.write(line)
						outFile2.write("\n")
						break
