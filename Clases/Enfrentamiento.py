import random
import time
from Clases.TextStyle import *


class Enfrentar:
    from Clases.Heroe import Heroe
    from Clases.Mounstro import Mounstro

    usuario: Heroe
    mounstro: Mounstro

    def __init__(self, _usuario, _mounstro):
        self.usuario = _usuario
        self.mounstro = _mounstro

    def iniciar_enfrentamiento(self):
        print(f"\n\tTe enfrentaras a un(a) {bcolors.BOLD}{self.mounstro.nombre}{bcolors.ENDC}, {bcolors.WARNING}preparate{bcolors.ENDC}")

        while True:
            time.sleep(1)
            print(f"\n\n\n{bcolors.BOLD}{self.mounstro.nombre}{bcolors.ENDC} se prepara para atacar")
            temporizador = 3
            while temporizador > 0:
                print("\t.")
                temporizador -= 1
                time.sleep(0.5)
            self.mounstro.atacar(self.usuario, self.mounstro.ataques[random.randrange(0, len(self.mounstro.ataques))])

            if self.usuario.vida < 0:
                break
            print("\t")
            time.sleep(1)
            ataque_usuario = ""
            while ataque_usuario != "1" and ataque_usuario != "2" and ataque_usuario != "3":
                print(f"\n\n{self.usuario.nombre} seleccione el ataque a usar\n"
                      f"\t{bcolors.OKGREEN}'1'{bcolors.ENDC} para usar {self.usuario.ataques[0]}\n"
                      f"\t{bcolors.OKGREEN}'2'{bcolors.ENDC} para usar {self.usuario.ataques[1]}\n"
                      f"\t{bcolors.OKGREEN}'3'{bcolors.ENDC} para usar {self.usuario.ataques[2]}\n"
                      "\nSeleccion: ")
                ataque_usuario = input().lower()
            ataque_usuario = int(ataque_usuario) - 1
            self.usuario.atacar(self.mounstro, self.usuario.ataques[ataque_usuario])
            if self.mounstro.vida < 0:
                break

        print("\n\n\t\tEnfrentamiento finalizado\n\n")
        print("Presiona 'Enter' para continuar")
        input()
        if self.usuario.vida > 0:
            print("\t.")
            time.sleep(0.5)
            if random.random() > 0.15:
                self.usuario.recibir_puntos_habilidad(random.randint(1, 3))
            print("\t.")
            time.sleep(0.5)
            if random.random() > 0.5:
                self.usuario.curar(random.randint(10, 50))
            print("\t.")
            time.sleep(0.5)
            if random.random() > 0.65:
                self.usuario.asignar_flechas(random.randint(1, 3))
            print("\t.\n\n")
            time.sleep(0.5)
            print(self.usuario)
            print("\n\nPresiona 'Enter' para continuar")
            input()
        return self.usuario.vida > 0
