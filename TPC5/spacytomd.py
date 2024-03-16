# pip install -U spacy
# python -m spacy download en_core_news_sm
import spacy

nlp = spacy.load("pt_core_news_lg")

text = ("O Rafael Picão Ferreira Correia gosta de cometer crimes, como fraude fiscal e despejar núcleos. ")
doc = nlp(text)


translate = {"ADJ":"adjetivo",
             "ADP":"proposição",
             "ADV":"advérbio",
             "AUX": "auxiliar",
            "CCONJ": "conjunção coordenativa",
            "DET": "determinante",
            "INTJ": "interjeção",
            "NOUN": "nome",
            "NUM": "número",
            "PART": "particula",
            "PRON": "pronome",
            "PROPN": "nome próprio",
            "PUNCT": "pontuação",
            "SCONJ": "conjunção subordinada",
            "SYM": "simbolo",
            "VERB": "verbo",
            "X": "outro"
             }


print("| Palavra | Tipo | Lema |\n|----|--------|----|")
current_entity = []
for token in doc:
    if token.ent_iob_ != "I" and current_entity:
        print("|","".join(current_entity),"|", "nome próprio","|","".join(current_entity),"|")
        current_entity = []
    if token.ent_iob_ == "B":            
        current_entity.append(token.text_with_ws)
    elif token.ent_iob_ == "I":
        current_entity.append(token.text_with_ws)
    elif token.pos_!="PUNCT":
        print("|",token.text,"|", translate[token.pos_],"|",token.lemma_,"|")
if current_entity:
    print("|","".join(current_entity),"|", "nome próprio","|","".join(current_entity),"|")
    