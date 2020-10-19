import random
import math
from typing import List
from Clases.Ataque import Ataque
from Clases.TextStyle import *


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

    def __str__(self):
        intro = "=====================\n"
        intro += f"Nombre: {bcolors.BOLD}{self.nombre}{bcolors.ENDC}\n"
        intro += f"Vida: {bcolors.WARNING}{self.vida}{bcolors.ENDC}\n"
        intro += f"Overall Magico: {self.ataque_magica}\n"
        intro += f"Overall Fisico: {self.ataque_fisica}\n"
        intro += "=====================\n"
        return intro

    def daniar(self, cantidad: float):
        print(f"{self.nombre} recibio {bcolors.FAIL}{cantidad}{bcolors.ENDC} de daño")
        self.vida -= cantidad
        self.evaluar_estado()
        pass

    def curar(self, cantidad: float):
        print(f"{self.nombre} ha recibido una curación por {bcolors.OKGREEN}{cantidad}{bcolors.ENDC} puntos")
        self.vida += cantidad
        if self.vida > 100:
            self.vida = 100
        self.evaluar_estado()
        pass

    def recibir_ataque(self, magia: float, fisico: float):
        danio_magico = self.defensa_magica - magia
        danio_fisico = self.defensa_fisica - fisico
        danio_pre_calculado = danio_magico + danio_fisico
        danio_total = 0 if danio_pre_calculado > 0 else danio_pre_calculado * random.uniform(1.0, 2.0) * 0.2
        danio_total = math.floor(danio_total)
        self.daniar(math.fabs(danio_total))

    def evaluar_estado(self):
        print(f"Vida restante de {bcolors.WARNING}{self.nombre}{bcolors.ENDC}: {bcolors.OKGREEN}{self.vida}{bcolors.ENDC}")
        if self.vida < 0:
            self.al_morir()
            return False
        return True

    def atacar(self, objetivo, ataque: Ataque):
        print(f"{bcolors.BOLD}{self.nombre}{bcolors.ENDC} ataca a {bcolors.WARNING}{objetivo.nombre}{bcolors.ENDC} con {bcolors.OKCYAN}{ataque.nombre}{bcolors.ENDC}")
        pass

    def al_morir(self):
        # evento por sobreescribir
        pass

