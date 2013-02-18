import sys
import re

## Input and Output file
inFile=open(sys.argv[1],"r")
outFile=open(sys.argv[2],"w")
## Separating the gene features
f1=inFile.readlines()
gene_lines=[]
commentline="###Gene"
counter=-1
for i in range(len(f1)):
	counter+=1
	if f1[i][0]=="#":
		continue
	else:
		cols=f1[i].strip().split('\t')
		desc=cols[8]
                feature=cols[2] # Takes the second column of the input gff3 file
                mydesc=desc.split(';') # Split the 9th column into individual fields
              	if feature=="gene":
			gene_lines.append(counter)
increment=0
for id in gene_lines:
	line_num=int(id)+increment
	f1.insert(line_num,commentline)
	increment+=1


## Dictionary of the IDs and the corresponsing auto-generated ID
mydict={}
count={"gene":0}
gene_features=[]
for line in f1:
	if line==commentline:
		outFile.write(line)
		outFile.write("\n")
		for item in gene_features:
			cols=item.strip().split('\t')
			mydesc=cols[8].split(';')
			for word in mydesc:
				if "ID=" in word:
					new=word.replace(id,new_id)
					item=item.replace(word,new)
				elif "Parent=" in word:
					new=word.replace(id,new_id)
					item=item.replace(word,new)	
			outFile.write(item)
		gene_features=[]
        elif line[0][0]=="#":
                continue
	else:
		cols=line.strip().split('\t')
                desc=cols[8]
                feature=cols[2] # Takes the second column of the input gff3 file
                mydesc=desc.split(';') # Split the 9th column into individual fields
                if feature=="gene":
                        for item in mydesc:
                                if "ID=" in item:
                                        temp=item.split('=')
                                        id=temp[1]
                                        count[feature]+=1
                                        new_id=feature+str(count[feature])
		gene_features.append(line)	
for item in gene_features:
	cols=item.strip().split('\t')
       	mydesc=cols[8].split(';')
      	for word in mydesc:
        	if "ID=" in word:
                	new=word.replace(id,new_id)
                       	item=item.replace(word,new)
             	elif "Parent=" in word:
                       	new=word.replace(id,new_id)
                      	item=item.replace(word,new)
	outFile.write(item)
