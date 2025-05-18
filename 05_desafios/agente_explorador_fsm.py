
import random
import time
from enum import Enum

class Estado(Enum):
    PARADO = 1
    EXPLORANDO = 2
    CARREGANDO = 3

class AgenteExplorador:
    def __init__(self):
        self.estado = Estado.PARADO
        self.energia = 100

    def perceber_obstaculo(self):
        return random.random() < 0.3

    def tomar_decisao(self):
        if self.estado == Estado.EXPLORANDO:
            self.energia -= 10
            if self.perceber_obstaculo() or self.energia <= 0:
                self.estado = Estado.PARADO
        elif self.estado == Estado.PARADO:
            if self.energia < 100:
                self.estado = Estado.CARREGANDO
            else:
                self.estado = Estado.EXPLORANDO
        elif self.estado == Estado.CARREGANDO:
            self.energia += 10
            if self.energia >= 100:
                self.estado = Estado.EXPLORANDO

    def agir(self):
        if self.estado == Estado.PARADO:
            print("[PARADO] Aguardando...")
        elif self.estado == Estado.EXPLORANDO:
            print("[EXPLORANDO] Procurando caminho...")
        elif self.estado == Estado.CARREGANDO:
            print("[CARREGANDO] Recarregando energia...")

    def executar(self, ciclos=10):
        for _ in range(ciclos):
            self.tomar_decisao()
            self.agir()
            time.sleep(1)

if __name__ == "__main__":
    agente = AgenteExplorador()
    agente.executar()
