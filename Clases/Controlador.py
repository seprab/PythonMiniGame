import time
import random
import sys
import os
import math
import csv


from Clases.Ataque import Ataque


def obtener_ataques_usuario():
    with open("../BDs/AtaquesHeroe.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        ataques = [Ataque(row[0], float(row[1]), float(row[2]), True if row[3] == "1" else False) for row in csv_reader]
        print(ataques)
        return ataques


obtener_ataques_usuario()


def obtener_ataques_mounstros():
    ataques = []
    return ataques


def cargar_mounstros():
    mounstros_cargados = []
    return mounstros_cargados


def salir():
    print("¡¡¡Adios!!!")
    sys.exit()


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


class Controlador:
    from Clases.Heroe import Heroe
    from Clases.Mounstro import Mounstro
    from Clases.Enfrentamiento import Enfrentar
    from typing import List

    piso: int
    usuario: Heroe
    mounstros: List[Mounstro]

    def iniciar(self):
        self.piso = 0
        self.configurar_usuario()
        self.configurar_mounstros()

    def configurar_usuario(self):
        nombre = ""

        while len(nombre) < 1 or nombre.count(" ") > 0:
            screen_clear()
            print("Por favor ingresa el nombre de tu heroe (sin espacios vacios): ")
            nombre = input()
        usuario = self.Heroe(nombre, obtener_ataques_usuario())
        print(f"¡Bienvenido {usuario.nombre} al reto de la torre!")
        print("Te encuentras en el reto de la torre donde deberas enfrentarte a un mounstro diferente por cada piso "
              "que logres avanzar. ¡Suerte!")

    def configurar_mounstros(self):
        self.mounstros = cargar_mounstros()
        ataques = obtener_ataques_mounstros()
        for mounstro in self.mounstros:
            indice_minimo = random.randint(0, math.floor(len(ataques) / 2))
            indice_maximo = random.randint(indice_minimo, len(ataques))
            mounstro.ataques = ataques[indice_minimo:indice_maximo]

    def avanzar_piso(self):
        print(f"Haz avanzado al piso {self.piso}")
        mounstro_enemigo = self.mounstros[random.randrange(0, len(self.mounstros))]
        mounstro_enemigo.nivel = self.piso
        enfrentar = self.Enfrentar(self.usuario, mounstro_enemigo)
        time.sleep(1)
        if enfrentar.iniciar_enfrentamiento():
            self.avanzar_piso()
            return
        else:
            salir()
            return
