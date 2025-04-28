class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def InserirComoPrimeiro(self, novo):
        if self.head is None:
            self.head = novo
            self.tail = novo
        else:
            novo.proximo = self.head
            self.head = novo
        self.size += 1

    
    def InserirComoUltimo(self, novo):
        if self.tail is None:
            self.head = novo
            self.tail = novo
        else:
            self.tail.proximo = novo
            self.tail = novo
        self.size += 1


    def InserirNaPosição(self, posicao, novo):
        if posicao < 0 or posicao > self.size:
            raise IndexError("Posição inválida")
        if posicao == 0:
            self.InserirComoPrimeiro(novo)
        elif posicao == self.size:
            self.InserirComoUltimo(novo)
        else:
            atual = self.head
            for _ in range(posicao - 1):
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo
            self.size += 1


    def InserirAntesDe(self, referencia, novo):
        if self.head is None:
            raise ValueError("Lista vazia")
        if self.head == referencia:
            self.InserirComoPrimeiro(novo)
            return
        atual = self.head
        while atual.proximo is not None and atual.proximo != referencia:
            atual = atual.proximo
        if atual.proximo is None:
            raise ValueError("Referência não encontrada")
        novo.proximo = atual.proximo
        atual.proximo = novo
        self.size += 1


    def InserirDepoisDe(self, referencia, novo):
        if self.head is None:
            raise ValueError("Lista vazia")
        atual = self.head
        while atual is not None and atual != referencia:
            atual = atual.proximo
        if atual is None:
            raise ValueError("Referência não encontrada")
        novo.proximo = atual.proximo
        atual.proximo = novo
        if atual == self.tail:
            self.tail = novo
        self.size += 1


    def RemoverPrimeiro(self):
        if self.head is None:
            raise ValueError("Lista vazia")
        removido = self.head
        self.head = self.head.proximo
        if self.head is None:
            self.tail = None
        self.size -= 1
        return removido
    

    def RemoverUltimo(self):
        if self.tail is None:
            raise ValueError("Lista vazia")
        if self.head == self.tail:
            removido = self.head
            self.head = None
            self.tail = None
        else:
            atual = self.head
            while atual.proximo != self.tail:
                atual = atual.proximo
            removido = self.tail
            atual.proximo = None
            self.tail = atual
        self.size -= 1
        return removido
    

    def RemoverNaPosição(self, posicao):
        if posicao < 0 or posicao >= self.size:
            raise IndexError("Posição inválida")
        if posicao == 0:
            return self.RemoverPrimeiro()
        elif posicao == self.size - 1:
            return self.RemoverUltimo()
        else:
            atual = self.head
            for _ in range(posicao - 1):
                atual = atual.proximo
            removido = atual.proximo
            atual.proximo = removido.proximo
            self.size -= 1
            return removido
        

    def RemoverElemento(self, elemento):
        if self.head is None:
            raise ValueError("Lista vazia")
        if self.head == elemento:
            return self.RemoverPrimeiro()
        atual = self.head
        while atual.proximo is not None and atual.proximo != elemento:
            atual = atual.proximo
        if atual.proximo is None:
            raise ValueError("Elemento não encontrado")
        removido = atual.proximo
        atual.proximo = removido.proximo
        if removido == self.tail:
            self.tail = atual
        self.size -= 1
        return removido
    

    def AcessaPrimeiro(self):
        if self.head is None:
            raise ValueError("Lista vazia")
        return self.head
    

    def AcessaUltimo(self):
        if self.tail is None:
            raise ValueError("Lista vazia")
        return self.tail
    

    def AcessaNaPosição(self, posicao):
        if posicao < 0 or posicao >= self.size:
            raise IndexError("Posição inválida")
        atual = self.head
        for _ in range(posicao):
            atual = atual.proximo
        return atual
    

    def AcessaElemento(self, elemento):
        if self.head is None:
            raise ValueError("Lista vazia")
        atual = self.head
        while atual is not None and atual != elemento:
            atual = atual.proximo
        if atual is None:
            raise ValueError("Elemento não encontrado")
        return atual
    

    def Exibir(self):
        atual = self.head
        while atual is not None:
            print(atual.valor, end=" -> ")
            atual = atual.proximo
        print("None")


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None



lk = LinkedList()
lk.InserirComoPrimeiro(Node(1))
lk.InserirComoUltimo(Node(2))
lk.InserirNaPosição(1, Node(3))
# Current list: 1 -> 3 -> 2
# Reference node for InserirAntesDe is Node(3)
lk.InserirAntesDe(lk.head.proximo, Node(4))
# Current list: 1 -> 4 -> 3 -> 2
# Reference node for InserirDepoisDe is Node(1)
lk.InserirDepoisDe(lk.head, Node(5))
# Current list: 1 -> 5 -> 4 -> 3 -> 2
lk.RemoverPrimeiro()
# Current list: 5 -> 4 -> 3 -> 2
lk.RemoverUltimo()
# Current list: 5 -> 4 -> 3
lk.AcessaPrimeiro()
lk.AcessaUltimo()
lk.Exibir()





