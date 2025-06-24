#python

""" grafo = {}
grafo ["voce"] = ["alice", "bob", "claire"]
entrada = input("Digite o nome de uma pessoa: ")
if entrada in grafo:
    print(grafo[entrada])
else:
    print("Pessoa não encontrada no grafo.")
 """ # desomentar código acima para testar

""" # python
grafo = {}
grafo["voce"] = ["anuj", "alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []
entrada = input("Digite o nome de uma pessoa: ")
if entrada in grafo: print(grafo[entrada])
else: print("Não encontrada no grafo.")
 """ # descomentar código acima para testar
# python
from collections import deque

d = deque()
print(d)  # deque([])

d.append(1)
d.append(2)
d.appendleft(0)
print(d)  # deque([0, 1, 2])

x = d.pop()
print(x)  # 2
print(d)  # deque([0, 1])

y = d.popleft()
print(y)  # 0
print(d)  # deque([1])

d2 = deque([4, 5, 6])
print(d2)  # deque([4, 5, 6])