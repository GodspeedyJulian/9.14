FileHandle=open("qbdata.txt", 'r')
FirstList=[]
LastList=[]
for Line in FileHandle.readlines():
    a=Line[-5:]
    if a[0]==' ':
        LastList.append(a[1:])
    else:
        LastList.append(a)
    Space=0
    for i in range(len(Line)):
        if Line[i]==' ':
            Space+=1
            if Space==2:
                FirstList.append(Line[:i])
                break
FileHandle.close()   
FileHandle=open('Newqbdata.txt','w')
for i in range(len(FirstList)):
    if float(LastList[i])>=60:
        #FileHandle.write(FirstList[i]+" got "+ LastList[i]+" which is higher than 60 ")
        FileHandle.write('{0} got {1}'.format(FirstList[i],LastList[i])+'\n')
FileHandle.close()   
