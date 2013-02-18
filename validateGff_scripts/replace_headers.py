import sys
import re

f1=open(sys.argv[1],"r")
f2=open(sys.argv[2],"r")
f3=open(sys.argv[3],"w")

mydict={}
gff_file=f1.readlines()
inFile=f2.readlines()
for line in inFile:
	line=line.rstrip("\n")
	words=line.split(":")
	mydict[words[0]]=words[1]

for line in gff_file:
	for key in mydict:
		if key in line:
			line=line.replace(key,mydict[key])
	f3.write(line)
