#!/usr/bin/python3
'''
NAME
    ex1 - Calculates word frequency in a text

SYNOPSIS
    ex1 [options] input_files
    options:
        -m 20 : Show 20 most common words
        -n : Order alphabeticaly

DESCRIPTION
'''
from jjcli import *
cl = clfilter("nm:", doc=__doc__)
# __doc__ é a primeira string num documento python, neste caso da linha 2 a 13


from collections import Counter
import sys,re


def tokenize(texto):
    palavras = re.findall(r'\w+(?:-\w+)?|[\;\,\.\:\!\?\_\-]+',texto)
    pontuacao = re.findall(r'',texto)
    print("Tem " + str(len(palavras))+ " palavras")
    return palavras

for txt in cl.text():
    lista_palavras = tokenize(txt)
    ocorr = Counter(lista_palavras)
    listCounter = list(ocorr.items())
    flag=False
    if "-n" in cl.opt:
        listCounter.sort()
    else:
        flag=True
        listCounter.sort(key = lambda a: -a[1])
    if "-m" in cl.opt:
        with open("output.txt","w") as f2:
            for word,frequency in listCounter[:int(cl.opt.get(-"m"))]:
                if flag:
                    f2.write(f"{frequency} : {word}\n")
                else:
                    f2.write(f"{word} : {frequency}\n")
    else:
        with open("output.txt","w") as f2:
            for word,frequency in listCounter:
                if flag:
                    f2.write(f"{frequency} : {word}\n")
                else:
                    f2.write(f"{word} : {frequency}\n")

        

        
