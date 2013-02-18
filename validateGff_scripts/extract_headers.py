import sys
import re

f1=open(sys.argv[1],"r")
f2=open(sys.argv[2],"w")
IDS=[]
GROUP=[]
#header_file=f1.readlines()
file=f1.readlines()
for line in file:
	if line.startswith("LOCUS"):
		m=re.findall(r'\bN\w+', line)
		id=m[0]
		IDS.append(id)
	elif line:
		for word in line.split():
			if word.startswith("Group"):
				grp=word
				group=grp.replace(",","")
				GROUP.append(group)
for i in range(len(IDS)):
	line=IDS[i]+":"+GROUP[i]+"\n"
	f2.write(line)

