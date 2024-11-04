#Abecedário

alfabeto="A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z"
alfabeto=alfabeto.replace(" ", "")
alfabeto=alfabeto.split(",")

#Vogais e Consoantes
vogais=list()
consoantes=list()
palavra=list()

#Começando a Gerar
for letra in alfabeto:
    if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        vogais.append(letra)
    else:
        consoantes.append(letra)

print(alfabeto)