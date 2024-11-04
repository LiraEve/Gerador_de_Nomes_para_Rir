import random

# Definir funções
def sortearLetraAlfabeto():
    LetraSorteada = alfabeto[random.randint(0, len(alfabeto) - 1)]
    tipo = None
    for letra in vogais:
        if LetraSorteada == letra:
            tipo = "vogal"
            break
    for letra in consoante:
        if LetraSorteada == letra:
            tipo = "consoante"
            break
    print(f'Letra sorteada: {LetraSorteada}, tipo: {tipo}')
    return LetraSorteada, tipo

# Abecedário
alfabeto = "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alfabeto = alfabeto.replace(" ", "")
alfabeto = alfabeto.split(",")

# Vogais e Consoantes
vogais = []
consoante = []
palavra = []

# Separando vogais e consoantes
for letra in alfabeto:
    if letra in ["A", "E", "I", "O", "U"]:
        vogais.append(letra)
    else:
        consoante.append(letra)

print(f'Lista de vogais: {vogais}, tamanho: {len(vogais)}')
print(f'Lista de consoantes: {consoante}, tamanho: {len(consoante)}')

# Tamanho da Palavra
tamanho = 6

# Formando Palavra
print(sortearLetraAlfabeto())
