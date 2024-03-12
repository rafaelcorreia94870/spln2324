#!/usr/bin/python3
'''
NAME
    wfreq - Calculates word frequency in a text

SYNOPSIS
    wfreq [options] input_files
    options:
        -m 20 : Show 20 most common words
        -n : Order alphabeticaly
        -o : Output to a file
        -i : Puts all the simmilar words in one word (Não: 2 , não:1 -> Não: 3)
        -r : Racios with dataset

DESCRIPTION

FILES:
    https://www.linguateca.pt/acesso/tokens/formas.cetenfolha.txt
'''
from jjcli import *
# __doc__ é a primeira string num documento python, neste caso da linha 2 a 13

__version__ = "0.0.1"


from collections import Counter
import sys,re


def tokenize(texto):
    palavras = re.findall(r'\w+(?:-\w+)?|[\;\,\.\:\!\?\_\-]+',texto)
    pontuacao = re.findall(r'',texto)
    print("Tem " + str(len(palavras))+ " palavras")
    return palavras

def simmilar(listCounter):
    for word,count in listCounter:
                if re.match('\w+',word):
                    pattern = "(?i)" + word
                    listsim = []
                    max = 0
                    maxkey = ""
                    for key,a in listCounter:
                        if re.match(pattern, key):
                            listsim.append((key,a))
                            if max < a:
                                max = a
                                maxkey = key
                    listsim.remove((maxkey,max))
                    oldmax = max
                    for sim,a in listsim:
                        max+=a
                        listCounter.remove((sim,a))
                    listCounter.remove((maxkey,oldmax))
                    listCounter.append((maxkey,max))


def main():
    
    cl = clfilter("o:nm:ir", doc=__doc__)
    """
    for line in cl.input():
        pass
    """
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
        if "-i" in cl.opt:
            simmilar(listCounter)
        if "-r" in cl.opt:
            total_frequency = sum(ocorr.values())
            with open("/home/rafael/4ano/2sem/spln2324/aula2/P1/word_freq/data/wordTablePT.txt", "r") as racio:
                frequencies = {}
                totalFreq = int(racio.readline())
                for line in racio.readlines():
                    word,frequency  = line.split(" ")
                    frequencies[word] = (int(frequency)/totalFreq)
            newList = []
            for word,frequency in listCounter:
                if word in frequencies:
                    r = frequency/total_frequency
                    if r/frequencies[word] >= -1:
                        newList.append((word,frequency))
            newList.sort(key = lambda x : x[1])
            listCounter= newList


        if "-m" in cl.opt:
            if "-o" in cl.opt:
                with open(cl.opt.get("-o"),"w") as f2:
                    for word,frequency in listCounter[:int(cl.opt.get("-m"))]:
                        if flag:
                            if "-r" in cl.opt:
                                f2.write(f"{(frequency/total_frequency)/frequencies[word]} : {word}\n")
                            else:
                                f2.write(f"{frequency} : {word}\n")
                        else:
                            if "-r" in cl.opt:
                                f2.write(f"{word} : {(frequency/total_frequency)/frequencies[word]}\n")
                            else:
                                f2.write(f"{word} : {frequency}\n")
            else:
                for word,frequency in listCounter[:int(cl.opt.get("-m"))]:
                        if flag:
                            if "-r" in cl.opt:
                                print(f"{(frequency/total_frequency)/frequencies[word]} : {word}\n")
                            else:
                                print(f"{frequency} : {word}\n")
                        else:
                            if "-r" in cl.opt:
                                print(f"{word} : {(frequency/total_frequency)/frequencies[word]}\n")
                            else:
                                print(f"{word} : {frequency}\n")

        else:
            if "-o" in cl.opt:
                with open(cl.opt.get("-o"),"w") as f2:
                    for word,frequency in listCounter:
                        if flag:
                            if "-r" in cl.opt:
                                f2.write(f"{(frequency/total_frequency)/frequencies[word]} : {word}\n")
                            else:
                                f2.write(f"{frequency} : {word}\n")

                        else:
                            if "-r" in cl.opt:
                                f2.write(f"{word} : {(frequency/total_frequency)/frequencies[word]}\n")
                            else:
                                f2.write(f"{word} : {frequency}\n")
            else:
                print(len(listCounter))
                for word,frequency in listCounter:
                    if flag:
                        if "-r" in cl.opt:
                            print(f"{(frequency/total_frequency)/frequencies[word]} : {word}\n")
                        else:
                            print(f"{frequency} : {word}\n")
                    else:
                        if "-r" in cl.opt:
                            print(f"{word} : {(frequency/total_frequency)/frequencies[word]}\n")
                        else:
                            print(f"{word} : {frequency}\n")



        
