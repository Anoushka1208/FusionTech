f=open("names.txt","r")
a=[]
for line in f:
    line=line.strip()
    a.append(line)

f.close()
a.sort()

g=open("sorted.txt","w")
for names in a:
    g.write(names + '\n')
g.close()
