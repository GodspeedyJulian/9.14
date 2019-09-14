import jieba

def getWords():
    with open("三国演义", 'r',\
              encoding = 'utf -8') as f:
        txt = f.read()
        words = jieba.lcut(txt)
        return words
words = getWords()
counts = {}
for i in words:
    if len(i) >= 2:
        counts[i] = counts.get(i, 0) + 1
listhills = list(counts.items())
listhills.sort(key=lambda x:x[1], reverse=True)
for i in range(50):
    word, counts = listhills[i]
    print('{0:<10}{1:>5}'.format(word, counts))
