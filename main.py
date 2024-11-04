import random

#Definir funções
def sortearLetraAlfabeto():
    LetraSorteada=alfabeto[random.randint(0, len(alfabeto)-1)]
    print(LetraSorteada)

#Abecedário

alfabeto="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alfabeto=alfabeto.replace(" ", "")
alfabeto=alfabeto.split(",")

#Vogais e Consoantes
vogais=list()
consoante=list()
palavra=list()

#Começando a Gerar
for letra in alfabeto:
    if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        vogais.append(letra)
    else:
        consoante.append(letra)
print(f'lista de vogais: {vogais}, tamanho: {len(vogais)}')
print(f'lista de consoantes: {consoante}, tamanho: {len(consoante)}')

#Tamanho da Palavra
tamanho=6

#Formando Palavra

sortearLetraAlfabeto()

print(alfabeto)