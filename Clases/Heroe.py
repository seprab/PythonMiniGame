from typing import List
from Clases.Entidades import Entidad
from Clases.Ataque import Ataque
from Clases.Mounstro import Mounstro


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
        pass

    def atacar(self, objetivo: Mounstro, ataque: Ataque):
        if ataque.requiere_flechas and self.numero_flechas <= 0:
            print("No tienes suficientes flechas para usar este ataque")
            return False
        elif ataque.requiere_flechas:
            self.numero_flechas -= 1
        Entidad.atacar(self, Mounstro, ataque)
        poder_magico_total = ataque.ataque_magica * self.ataque_magica
        poder_fisico_total = ataque.ataque_fisica * self.ataque_fisica * self.precision
        objetivo.recibir_ataque(poder_magico_total, poder_fisico_total)
        return True

    def usar_puntos_habilidad(self):
        print(f"{self.nombre} tienes {self.puntos_habilidad} disponibles, ¿deseas usarlos?\n Ingrese 'Si' o 'No':")
        seleccion_usuario = input().lower()
        if seleccion_usuario == "no":
            return
        elif seleccion_usuario != "si":
            print("Haz ingresado un valor de entrada no valido, presta atención a las instrucciones:")
            self.usar_puntos_habilidad()

        print(
            "Selecciona:\n'1' para aumentar la estadistica de fuerza fisica\n'2' para aumentar la estadistica "
            "mágica\n'3' para aumentar la estadistica de precisión\n")
        while self.puntos_habilidad > 0:
            try:
                print("Realiza tu selección: ")
                seleccion_usuario = int(input())
                if seleccion_usuario < 1 or seleccion_usuario > 3:
                    continue
                else:
                    if seleccion_usuario == 1:
                        self.defensa_fisica += 0.1
                        self.ataque_fisica += 1
                    elif seleccion_usuario == 2:
                        self.defensa_magica += 0.1
                        self.ataque_magica += 1
                    else:
                        self.precision += 0.5
                    self.puntos_habilidad -= 1
            except ValueError:
                print("Haz ingresado un valor no valido.\n")
                continue
        pass

    def recibir_puntos_habilidad(self, cantidad: int):
        print(f"Has recibido {cantidad} puntos de habilidad.\n")
        self.usar_puntos_habilidad()
        pass

    def al_morir(self):
        print("¡Has muerto!")
        pass
