import poetry as p 
"""
print(p.chain_of_n_words(3))
print(p.poemWords)
"""

def nlik(n=4, e=5):
    print()
    print("İlham alınıyor...")
    print(f"Her biri {e} kelimeli {n} dize:")
    print()
    for i in range(n):
        print(p.chain_of_n_words(e))
    print()

nlik(4, 8)