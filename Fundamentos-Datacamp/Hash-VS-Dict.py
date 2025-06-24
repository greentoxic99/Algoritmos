# em python, qual é a diferença entre dicionarios e hashes?
# Em Python, dicionários e hashes são frequentemente usados de forma intercambiável, mas há algumas nuances a considerar.
# Dicionários são uma estrutura de dados embutida em Python que armazena pares chave-valor.
# Eles são implementados como tabelas de hash, o que significa que as chaves são mapeadas para valores usando uma função de hash.
# A principal diferença é que "hash" é um termo mais genérico que se refere a qualquer estrutura de dados que usa uma função de hash para mapear chaves a valores,
# enquanto "dicionário" é uma implementação específica dessa ideia em Python.
# Dicionários são mutáveis, o que significa que você pode adicionar, remover ou alterar pares chave-valor após a criação.
# Além disso, os dicionários em Python mantêm a ordem de inserção das chaves desde o Python 3.7, o que significa que você pode iterar sobre eles na ordem em que as chaves foram adicionadas.
# Exemplo de uso de dicionários em Python
def exemplo_dicionario():
    # Criando um dicionário
    pessoa = {
        "nome": "João",
        "idade": 30,
        "cidade": "São Paulo"
    }

    # Acessando valores
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade: {pessoa['cidade']}")

    # Adicionando um novo par chave-valor
    pessoa["profissão"] = "Engenheiro"
    print(f"Profissão: {pessoa['profissão']}")

    # Iterando sobre o dicionário
    for chave, valor in pessoa.items():
        print(f"{chave}: {valor}")
# Chamando a função de exemplo
exemplo_dicionario()
# Em resumo, dicionários são uma implementação específica de uma estrutura de dados baseada em hash em Python,
# e eles oferecem uma maneira eficiente de armazenar e acessar dados usando chaves únicas.
# Dicionários são amplamente utilizados em Python devido à sua flexibilidade e eficiência.
# Eles são uma parte fundamental da linguagem e são usados em muitas aplicações, desde armazenamento de configurações até manipulação de dados complexos.
# Dicionários são uma parte fundamental da linguagem Python e são amplamente utilizados em muitas aplicações.
# Eles são uma parte fundamental da linguagem e são amplamente utilizados em muitas aplicações.
if __name__ == "__main__":
    exemplo_dicionario()
    # Agora, hashes são um conceito mais amplo que pode ser implementado de várias maneiras em diferentes linguagens de programação.
    # Em Python, o termo "hash" geralmente se refere à função de hash usada para mapear chaves a valores em dicionários.
    # No entanto, Python também possui outras estruturas de dados que usam hashing, como conjuntos (sets) e tipos imutáveis como frozenset.
    # Portanto, enquanto todos os dicionários são baseados em hashing, nem todas as estruturas de dados que usam hashing são dicionários.
    # Agora, vamos ver um exemplo de uso de hashing com conjuntos (sets) em Python.
def exemplo_set():
    # Criando um conjunto
    numeros = {1, 2, 3, 4, 5}

    # Adicionando um elemento
    numeros.add(6)
    print(f"Números após adição: {numeros}")

    # Removendo um elemento
    numeros.remove(3)
    print(f"Números após remoção: {numeros}")

    # Verificando se um elemento está no conjunto
    if 4 in numeros:
        print("O número 4 está no conjunto.")

    # Iterando sobre o conjunto
    for numero in numeros:
        print(f"Número: {numero}")
