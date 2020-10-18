from Clases.Heroe import Heroe
from Clases.Mounstro import Mounstro
from Clases.Enfrentamiento import Enfrentar
from typing import List
import time
import random
import sys
import os
import math

piso: int
usuario: Heroe
mounstros: List[Mounstro]


def iniciar():
    global piso
    piso = 0
    configurar_usuario()
    configurar_mounstros()


def configurar_usuario():
    global usuario
    nombre = ""

    while len(nombre) < 1 or nombre.count(" ") > 0:
        screen_clear()
        print("Por favor ingresa el nombre de tu heroe (sin espacios vacios): ")
        nombre = input()
    usuario = Heroe(nombre, obtener_ataques_usuario())
    print(f"¡Bienvenido {usuario.nombre} al reto de la torre!")
    print("Te encuentras en el reto de la torre donde deberas enfrentarte a un mounstro diferente por cada piso que "
          "logres avanzar. ¡Suerte!")


def configurar_mounstros():
    global mounstros
    mounstros = cargar_mounstros()
    ataques = obtener_ataques_mounstros()
    for mounstro in mounstros:
        indice_minimo = random.randint(0, math.floor(len(ataques) / 2))
        indice_maximo = random.randint(indice_minimo, len(ataques))
        mounstro.ataques = ataques[indice_minimo:indice_maximo]


def avanzar_piso():
    global piso
    global usuario
    global mounstros
    print(f"Haz avanzado al piso {piso}")
    mounstro_enemigo = mounstros[random.randrange(0, len(mounstros))]
    mounstro_enemigo.nivel = piso
    enfrentar = Enfrentar(usuario, mounstro_enemigo)
    time.sleep(1)
    if enfrentar.iniciar_enfrentamiento():
        avanzar_piso()
        return
    else:
        salir()
        return


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


def salir():
    print("¡¡¡Adios!!!")
    sys.exit()


def obtener_ataques_usuario():
    ataques = []
    return ataques


def obtener_ataques_mounstros():
    ataques = []
    return ataques


def cargar_mounstros():
    mounstros_cargados = []
    return mounstros_cargados


iniciar()
