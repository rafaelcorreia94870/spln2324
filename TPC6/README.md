# Script para encontrar o(s) melhor(es) amigo(s) de cada personagem

## Autor
Rafael Picão Ferreira Correia

## UC
SPLN

## Resumo


A script analisa as várias entidades presentes num texto e identifica os seus "melhores amigos".

Para tal usei a biblioteca `Spacy`, que permite identificar as entidades. Isto é feito da seguinte maneira:  para cada frase, se existirem 2 ou mais entidades, a relação entre elas é guardada como uma "amizade".

Existe um dicionário que relaciona todas as entidades a um respetivo Counter cuja chave é outra entidade e o valor o número de vezes que as duas aparecem numa mesma frase.



## Execução

```bash 
pip install -U spacy
python -m spacy download pt_core_news_lg
python3 findamigos.py > HP.txt
```