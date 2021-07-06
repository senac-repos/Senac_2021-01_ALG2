"""
Implementar uma pilha de objetos Livro.
O objeto Livro também deve possuir os atributos id, título e autor.
O atributo autor será utilizado para armazenar um objeto do tipo Autor. A classe Autor deve possuir o atributo
fortemente privado id e o atributo público nome.
O sistema deverá possuir métodos para inserir e para retirar livros da pilha.
"""

from Classes.Pilha import Pilha
from Classes.Livro import Livro
from Classes.Autor import Autor

pilha = Pilha()

autor1 = Autor(1, 'Autor 1')
autor2 = Autor(2, 'Autor 2')
autor3 = Autor(3, 'Autor 3')

livro1 = Livro(1, 'Livro 1', autor1)
livro2 = Livro(2, 'Livro 2', autor2)
livro3 = Livro(3, 'Livro 3', autor1)
livro4 = Livro(4, 'Livro 4', autor3)

pilha.adicionar(livro1)
pilha.adicionar(livro2)
pilha.adicionar(livro3)
pilha.adicionar(livro4)

pilha.remover()
pilha.remover()
