# Script para ter uma tabela informativa de uma frase

## Autor
Rafael Picão Ferreira Correia

## UC
SPLN

## Resumo

É necessário correr estes comandos:

pip install -U spacy

python -m spacy download en_core_news_sm

Peguei num texto (neste caso dentro do ficheiro da script), e por cada token da frase tratei-o dependente do seu tipo. Ignorei pontuação e juntei os nomes que pertencem uns aos outros. Isto pode ser feito com o token.ent_iob_, aonde se for B é o inicio de um nome e I se está contido num nome.

Comando : python3 spacytomd.py > md.md
