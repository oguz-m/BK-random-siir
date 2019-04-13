from random import randint


f=open("s.txt", "r")
List = f.readlines()
f.close()

del List[1:-1:2]

"""
for i in range(3):
	print(List[randint(0, len(List)-1)])
"""

verbs = []
nouns = []
miscell = []

for sent in List:
	words_list = sent.split()
	
	if not words_list == []:
		for word in words_list:
			
			if len(word) >= 3:
				if word[-1] == "." or word[-1] == '"' or word[-1] == "?" or word[-1] == "!":
					verbs.append(word.replace('"', ''))
				elif word[0].isupper() or word[0] == '"':
					nouns.append(word.replace('"', ''))
				else:
					miscell.append(word.replace('"', ''))


		#if words_list[0] != '-' and words_list[0] != '"-':
		#	nouns.append(words_list[0])

"""
print(verbs)
print("\n\n\n\n")
print(nouns)
print("\n\n\n\n")
print(miscell)
"""

def r(a):
	return a[randint(0, len(a)-1)]

def r123(a):
	i = randint(0, len(a)-4)
	return a[i]+" "+a[i+1]+" "+a[i+2]


def rand_micro_sfstory():

	print(r(nouns), r123(miscell), r(verbs))
	print(r(verbs).capitalize().replace(".",","), r123(miscell), r(nouns).lower()+".")
	
	a = r(verbs).capitalize().replace(".",",")
	
	print(a,a,a.replace(",","."))
	print(r(miscell).capitalize(), r(nouns).lower()+".")


rand_micro_sfstory()
