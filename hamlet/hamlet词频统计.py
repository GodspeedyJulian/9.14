print("there are:")
def getText():
    with open (r'hamlet.txt',"r",\
               encoding= 'utf-8')as f:
        txt = f.read()
        for i in '~!@#$%^&*()_+-={}|:"<>?[]\;,./—':
            txt = txt.replace(i, ' ')
        return txt
txt= getText()
words=txt.split()
counts={}
for i in words:
    counts[i] = counts.get(i, 0) + 1
 
listhills = list(counts.items())
listhills.sort(key=lambda x:x[1], reverse=True)
 
for i in range(10):
    word, counts = listhills[i]
    print('{0:<10}{1:>5}'.format(word, counts))

print("in hamlet.txt")


    
