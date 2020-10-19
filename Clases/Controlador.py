import time
import random
import sys
import os
import math
import csv

from Clases.Ataque import Ataque
from Clases.Heroe import Heroe
from Clases.Mounstro import Mounstro
from Clases.Enfrentamiento import Enfrentar
from Clases.TextStyle import *
from typing import List


def obtener_ataques_usuario():
    with open("BDs/AtaquesHeroe.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        ataques = [Ataque(row[0], float(row[1]), float(row[2]), True if row[3] == "1" else False) for row in csv_reader]
        return ataques


def obtener_ataques_mounstros():
    with open("BDs/AtaquesMounstro.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        ataques = [Ataque(row[0], float(row[1]), float(row[2]), False) for row in csv_reader]
        return ataques


def cargar_mounstros():
    with open("BDs/ListadoMounstros.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        mounstros_cargados = [Mounstro(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4])) for row in
                              csv_reader]
        return mounstros_cargados


def salir():
    print("\n\n\t\t¡¡¡Adios!!!")
    time.sleep(3)
    sys.exit()


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


class Controlador:
    piso: int
    usuario: Heroe
    mounstros: List[Mounstro]

    def __init__(self):
        self.piso = 0
        self.usuario = None
        self.mounstros = None

    def iniciar(self):
        self.piso = 0
        self.configurar_usuario()
        self.configurar_mounstros()
        screen_clear()
        print(f"\t{bcolors.HEADER}{self.usuario.nombre}, {bcolors.BOLD}¡Bienvenido al reto de la torre! {bcolors.ENDC}{bcolors.ENDC}\n\n")
        print("Deberas enfrentarte a un mounstro diferente por cada piso "
              "que logres avanzar. Tienes una espada que hace daño fisico, una vara que hace daño magico y un arco "
              f"que utiliza flechas.\n\n\n{self.usuario}\n\n\t¡Suerte!\n\nPresiona 'enter' para continuar")
        input()
        self.avanzar_piso()

    def configurar_usuario(self):
        nombre = ""
        while len(nombre) < 1 or nombre.count(" ") > 0:
            screen_clear()
            print(f"\t\t{bcolors.HEADER}¡¡¡reto de la torre!!!{bcolors.ENDC}\n")
            print(f"Por favor ingresa el nombre de tu heroe {bcolors.WARNING}(sin espacios vacios){bcolors.ENDC}: ")
            nombre = input()
        self.usuario = Heroe(nombre, obtener_ataques_usuario())

    def configurar_mounstros(self):
        self.mounstros = cargar_mounstros()
        ataques = obtener_ataques_mounstros()
        for mounstro in self.mounstros:
            indice_minimo = random.randint(0, math.floor(len(ataques) / 2))
            indice_maximo = random.randint(indice_minimo, len(ataques))
            mounstro.ataques = ataques[indice_minimo:indice_maximo]

    def avanzar_piso(self):
        self.piso += 1;
        print(f"\n\n{bcolors.OKCYAN}Haz avanzado al piso {self.piso}{bcolors.ENDC}")
        mounstro_enemigo = self.mounstros[random.randrange(0, len(self.mounstros))]
        mounstro_enemigo.nivel = self.piso
        enfrentar = Enfrentar(self.usuario, mounstro_enemigo)
        if enfrentar.iniciar_enfrentamiento():
            self.avanzar_piso()
            return
        else:
            print(f"\t\t{bcolors.WARNING}Llegaste al piso: {self.piso}{bcolors.ENDC}")
            salir()
            return
