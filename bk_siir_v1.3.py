from random import randint
import sys


f=open("s.txt", "r")
List = f.readlines() # elements are string sentences
f.close()

words_list = []
yuklem = []
ozne = []
diger = []
ayrilma = []
bulunma = []
arak = []
soru_ed = []

for sent in List:
	for word in sent.split():
		if not word.endswith("-") and not word.endswith("+"):
			words_list.append(word.replace('"', '').replace(",", "").replace("(","").replace(")",""))

#print(words_list)
yuklem_tuple = (".", "?", "!", "tı", "ti", "tu", "tü", "dı", "di", "du", "dü", "mış", "miş", "muş", "müş")

for word in words_list:
	if word.endswith(("dan", "den", "tan", "ten")):
		ayrilma.append(word)
	if word.endswith(("da", "de", "ta", "te")):
		bulunma.append(word)
	if word.endswith(("erek", "arak")):
		arak.append(word)
	if word.endswith(("mı?", "mi?", "mu?", "mü?")):
		soru_ed.append(word)
	elif word.endswith(yuklem_tuple) or word.endswith(yuklem_tuple, 0, -1):
		yuklem.append(word)
	elif word[0].isupper():
		ozne.append(word)
	else:
		diger.append(word)


def r(l):
	# a rondom element of the given list l
	return l[randint(0, len(l)-1)]


def r123(l, n=3):
	# n random consecutive elements of the given list l
	s = ""
	if n < len(l)-2:
		i = randint(0, len(l)-(n+1))
		for a in range(0,n):
			s = s+l[i+a]+" "
	return s[:-1]
	#return l[i]+" "+l[i+1]+" "+l[i+2]


def kuralli(length=5, opt="consecutive"):
	ozn = r(ozne)
	
	if opt == "consecutive":
		nsn = r123(diger, (length-2))
	elif opt == "random":
		nsn = ""
		for i in range(length-2):
			nsn = nsn+r(diger)+" "
		nsn = nsn[:-1]
	
	ykl = r(yuklem).lower()

	return ozn+" "+nsn+" "+ykl



def devrik(length=5, opt="consecutive"):
	ykl = r(yuklem).capitalize().replace(".",",").replace("?", "?,").replace("!", "!,")
	
	if opt == "consecutive":
		nsn = r123(diger, (length-2))
	elif opt == "random":
		nsn = ""
		for i in range(length-2):
			nsn = nsn+r(diger)+" "
		nsn = nsn[:-1]

	ozn = r(ozne).lower()+"."
	
	return ykl+" "+nsn+" "+ozn



def ucleme_virgullu(typ=yuklem, length=3):
	a = r(typ).capitalize().replace(".",",").replace("?", "?,").replace("!", "!,")
	s = ""
	if length < len(typ)-2:
		for i in range(length):
			s = s+a+" "
	return s[:-2]+"."


def var1():
	print(kuralli(5, "consecutive"))
	print(devrik(5, "consecutive"))
	print(r(arak).capitalize(), r123(diger, 2), r(bulunma).lower()+".")
	print(r(ayrilma).capitalize()+",")
	print(r(ozne), r(yuklem).lower())


def var2():
	print(kuralli(5, "consecutive"))
	print(devrik(5, "consecutive"))
	print(ucleme_virgullu(yuklem, 3))
	print(r(diger).capitalize(), r(ozne).lower()+".")

var2()

"""
sys.stdout=open("randomm.txt","a+", errors="ignore")
print("\n")
var1()
sys.stdout.close()
"""

print(len(yuklem))
print(len(ozne))
print(len(diger))
print(len(ayrilma))
print(len(bulunma))
print(len(arak))
print(len(soru_ed))
