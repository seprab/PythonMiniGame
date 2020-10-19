from typing import List
from Clases.Entidades import Entidad
from Clases.Ataque import Ataque
from Clases.TextStyle import *


class Heroe(Entidad):
    precision: float
    numero_flechas: int
    puntos_habilidad: int

    def __init__(self, _nombre: str, _ataques: List[Ataque]):
        Entidad.__init__(self, _nombre, _ataques)
        self.defensa_fisica = 1
        self.defensa_magica = 1
        self.ataque_fisica = 10
        self.ataque_magica = 10
        self.precision = 1.2
        self.puntos_habilidad = 0
        self.numero_flechas = 3
        pass

    def __str__(self):
        info = Entidad.__str__(self)
        info += f"Overall Precisión: {self.precision}\n"
        info += f"Flechas restantes: {self.numero_flechas}\n"
        info += f"Puntos habilidad restantes: {self.puntos_habilidad}\n"
        return info

    def atacar(self, objetivo, ataque: Ataque):
        if ataque.requiere_flechas and self.numero_flechas <= 0:
            print(f"{bcolors.WARNING}No tienes suficientes flechas para usar este ataque{bcolors.ENDC}")
            return False
        elif ataque.requiere_flechas:
            self.numero_flechas -= 1
        Entidad.atacar(self, objetivo, ataque)
        poder_magico_total = ataque.ataque_magica * self.ataque_magica
        poder_fisico_total = ataque.ataque_fisica * self.ataque_fisica * self.precision
        objetivo.recibir_ataque(poder_magico_total, poder_fisico_total)
        return True

    def usar_puntos_habilidad(self):
        print(f"{bcolors.BOLD}{self.nombre}{bcolors.ENDC} tienes {bcolors.OKCYAN}{self.puntos_habilidad}{bcolors.ENDC} disponibles, ¿deseas usarlos?\n Ingrese {bcolors.OKGREEN}'Si'{bcolors.ENDC} o {bcolors.WARNING}'No'{bcolors.ENDC}:")
        seleccion_usuario = input().lower()
        if seleccion_usuario == "no":
            print("\n")
            return
        elif seleccion_usuario != "si":
            print(f"Haz ingresado un valor de entrada no valido, {bcolors.WARNING}presta atención a las instrucciones:{bcolors.ENDC}")
            self.usar_puntos_habilidad()

        print(
            f"Selecciona:\n{bcolors.OKCYAN}'1'{bcolors.ENDC} para aumentar la estadistica de fuerza fisica\n{bcolors.OKCYAN}'2'{bcolors.ENDC} para aumentar la estadistica "
            f"mágica\n{bcolors.OKCYAN}'3'{bcolors.ENDC} para aumentar la estadistica de precisión\n")
        while self.puntos_habilidad > 0:
            try:
                print(f"Puntos restantes: {self.puntos_habilidad}. \t Realiza tu selección para usar un punto de "
                      f"habilidad: ")
                seleccion_usuario = int(input())
                if seleccion_usuario < 1 or seleccion_usuario > 3:
                    continue
                else:
                    if seleccion_usuario == 1:
                        self.defensa_fisica += 0.1
                        self.ataque_fisica += 1
                        print("Acabas de asignar un punto al atributo físico.")
                    elif seleccion_usuario == 2:
                        self.defensa_magica += 0.1
                        self.ataque_magica += 1
                        print("Acabas de asignar un punto al atributo mágico.")
                    else:
                        self.precision += 1
                        print("Acabas de asignar un punto al atributo precisión.")
                    self.puntos_habilidad -= 1
            except ValueError:
                print("Haz ingresado un valor no valido.\n")
                continue
        pass

    def recibir_puntos_habilidad(self, cantidad: int):
        print(f"Has recibido {bcolors.OKGREEN}{cantidad}{bcolors.ENDC} puntos de habilidad.\n")
        self.puntos_habilidad += cantidad
        self.usar_puntos_habilidad()
        pass

    def asignar_flechas(self, cantidad: int):
        print(f"Acabas de recibir {bcolors.OKGREEN}{cantidad}{bcolors.ENDC}  flechas.\n")
        self.numero_flechas += cantidad

    def al_morir(self):
        print(f"\n\n\t\t{bcolors.FAIL}¡{self.nombre} has muerto!{bcolors.ENDC}")
        pass
