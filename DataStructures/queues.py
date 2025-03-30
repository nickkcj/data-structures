from typing import Deque, Any
from collections import deque

class Queue:
    def __init__(self, tamanho: None):
        self.fila = deque(maxlen=tamanho)
        
    def inserir(self, valor: Any) -> None:
        self.fila.append(valor)

    def remover(self) -> Any:
        return self.fila.popleft()
    
    def vazia(self):
        return len(self.fila) == 0
    
    def tamanho(self):
        return len(self.fila)
