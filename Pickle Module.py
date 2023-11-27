import pickle as p
#DUMP IN A NEW TXT IN BYTES
l=[10,20,30,40,50]
file = open("pickle.txt","wb")
p.dump(l,file)
file.close()

#WB --> Write Byte
#RB --> Read Byte
f = open("a.txt", "rb")
aa = p.load(f)
print(aa)
f.close()