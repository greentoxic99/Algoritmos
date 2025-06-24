# python

""" Você recebe duas strings word1 e word2. Mescle as strings adicionando letras em ordem alternada,
 começando com word1.
 Se uma string for maior que a outra, anexe as letras adicionais ao final da string mesclada.

Retorna a string mesclada.


Exemplo 1:

Entrada: palavra1 = "abc", palavra2 = "pqr"
 Saída: "apbqcr"
 Explicação:  A sequência mesclada será mesclada da seguinte forma:
palavra1: abc
palavra2: pqr
mesclado: apbqcr """
#Descomente para teste com usuario
""" word1 = input("Digite a primeira palavra: ")
tam_word1 = len(word1)
word2 = input("Digite a segunda palavra: ") """
word1 = "abc"
word2 = "pqr"

#verificar se o tamanho de cada string é igual
if len(word1) == len(word2):
    print("As duas palavras têm o mesmo tamanho.\n")
    print("string alternada: ", *[word1[i] + word2[i] for i in range(len(word1))], sep="")
elif len(word1) > len(word2):
    print("A primeira palavra é maior que a segunda.\n")
    print("palavra1 alternada: ", *[word1[i] + word2[i] for i in range(len(word2))], sep="")
    print("palavra2: ", word2)
else:
    print("A segunda palavra é maior que a primeira.\n")


#print("letras da primeira palavra: ", *word1[0:tam_word1], sep="\n")