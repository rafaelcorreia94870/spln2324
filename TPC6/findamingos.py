# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import sys
from spacy import displacy
from collections import Counter

nlp = spacy.load("pt_core_news_lg")

with open(sys.argv[1]) as file:
    content = file.read()

doc = nlp(content)



with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)
        
names = {}

for sentence in doc.sents:
    names_sentence = set()
    for token in sentence:
        if token.pos_=="PROPN":
            names_sentence.add(token.text)
    for n1 in names_sentence:
        if n1 not in names:
            names[n1] = Counter()
        for n2 in names_sentence:
            if n1!=n2:
                names[n1][n2]+=1

for name,friends in names.items():
    if friends.values():
        max_val = max(friends.values())
        bestie = list(filter(lambda x: friends[x] == max_val, friends))
        print("Best friend of",name,":",bestie,f"({max_val})")
    