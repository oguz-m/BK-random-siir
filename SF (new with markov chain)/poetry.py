import numpy as np 

poems = open("mikro_tr.txt", encoding="utf-8").read()

poemWords_temp = poems.split()
poemWords = []

def normalizeWord(w):
    w_new = ""
    for l in w.lower():
        if l in "abcçdefgğhıijklmnoöprsştuüvyzqxwßä":
            w_new += l
    return w_new

for w in poemWords_temp:
    if normalizeWord(w) != "":
        poemWords.append(normalizeWord(w))  


def makePairs(poemwords):
    """
    assumes poemWords a list
    returns a generator
    """
    for i in range(len(poemWords)-1):
        yield (poemWords[i], poemWords[i+1])

pairs = makePairs(poemWords)
"""
pairs is a generator(an iterable like a list, except deletes itself after the first iteration(e.g. for loop)) made of tuples
"""

wordDict = {}
"""
str --> list
"""

for (word1,word2) in pairs:
    if word1 in wordDict.keys():
        wordDict[word1].append(word2)
    else:
        wordDict[word1] = [word2] # a list


def chain_of_n_words(nWords):
    firstWord = np.random.choice(poemWords)

    chain = [firstWord]

    for i in range(nWords-1):
        chain.append(np.random.choice(wordDict[chain[-1]]))
    return " ".join(chain)


if __name__ == "__main__":
    print()
    print(chain_of_n_words(5))
    print()


"""
temp = 0
for x in range(0,len(chain),5):
    print(" ".join(chain[temp:x]))
    temp = x
"""









