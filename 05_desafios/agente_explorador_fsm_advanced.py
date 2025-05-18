import random
import time
import json
from enum import Enum
from datetime import datetime

class Estado(Enum):
    PARADO = 1
    EXPLORANDO = 2
    CARREGANDO = 3

class AgenteExplorador:
    def __init__(self, log_file='log_agente.json'):
        self.estado = Estado.PARADO
        self.energia = 100
        self.log_file = log_file
        self.logs = []

    def perceber_obstaculo(self):
        return random.random() < 0.25

    def tomar_decisao(self):
        transicao = {"timestamp": str(datetime.utcnow()), "estado_atual": self.estado.name, "energia": self.energia}

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

        transicao["novo_estado"] = self.estado.name
        transicao["nova_energia"] = self.energia
        self.logs.append(transicao)

    def agir(self):
        if self.estado == Estado.PARADO:
            print("[PARADO] Aguardando...")
        elif self.estado == Estado.EXPLORANDO:
            print("[EXPLORANDO] Explorando ambiente...")
        elif self.estado == Estado.CARREGANDO:
            print("[CARREGANDO] Carregando energia...")

    def executar(self, ciclos=10):
        for _ in range(ciclos):
            self.tomar_decisao()
            self.agir()
            time.sleep(0.5)

        with open(self.log_file, 'w') as f:
            json.dump(self.logs, f, indent=2)

if __name__ == "__main__":
    agente = AgenteExplorador()
    agente.executar()