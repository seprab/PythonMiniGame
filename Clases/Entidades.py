import random
from typing import List
from Clases.Ataque import Ataque


class Entidad:
    nombre: str
    vida: float
    defensa_fisica: float
    defensa_magica: float
    ataque_fisica: float
    ataque_magica: float
    ataques: List[Ataque]

    def __init__(self, _nombre: str, _ataques: List[Ataque]):
        self.nombre = _nombre
        self.ataques = _ataques
        self.vida = 100
        pass

    def daniar(self, cantidad: float):
        self.vida -= cantidad
        self.evaluar_estado()
        pass

    def curar(self, cantidad: float):
        self.vida += cantidad
        if self.vida > 100:
            self.vida = 100
        self.evaluar_estado()
        pass

    def recibir_ataque(self, magia: float, fisico: float):
        danio_magico = self.defensa_magica - magia
        danio_fisico = self.defensa_fisica - fisico
        danio_pre_calculado = danio_magico + danio_fisico
        danio_total = 0 if danio_pre_calculado > 0 else danio_pre_calculado * random.uniform(1.0, 2.0)
        self.daniar(danio_total)

    def evaluar_estado(self):
        if self.vida < 0:
            self.al_morir()
            return False
        return True

    def atacar(self, objetivo, ataque: Ataque):
        print(f"{self.nombre} ataca a {objetivo.nombre} con {ataque.nombre}")
        pass

    def al_morir(self):
        # evento por sobreescribir
        pass
