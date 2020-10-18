import random
import time


class Enfrentar:
    from Clases.Heroe import Heroe
    from Clases.Mounstro import Mounstro

    usuario: Heroe
    mounstro: Mounstro

    def __init__(self, _usuario, _mounstro):
        self.usuario = _usuario
        self.mounstro = _mounstro

    def iniciar_enfrentamiento(self):
        print(f"Te enfrentaras a un(a) {self.mounstro.nombre}, preparate")
        time.sleep(3)
        while True:
            print(f"{self.mounstro.nombre} se prepara para atacar")
            temporizador = 3
            while temporizador > 0:
                print(".")
                temporizador -= 1
                time.sleep(2)
            self.mounstro.atacar(self.usuario, self.mounstro.ataques[random.randrange(0, len(self.mounstro.ataques))])

            if not self.usuario.evaluar_estado():
                break

            ataque_usuario = ""
            while ataque_usuario != "1" or ataque_usuario != "2" or ataque_usuario != "3":
                print("Por favor seleccione el ataque a usar\n"
                      f"'1' para usar {self.usuario.ataques[0].nombre}\n"
                      f"'2' para usar {self.usuario.ataques[1].nombre}\n"
                      f"'3' para usar {self.usuario.ataques[2].nombre}\n"
                      "Seleccion: ")
                ataque_usuario = input().lower()
            ataque_usuario = int(ataque_usuario) - 1
            self.usuario.atacar(self.mounstro, self.usuario.ataques[ataque_usuario])

            if not self.mounstro.evaluar_estado():
                break

        print("Enfrentamiento finalizado")
        if self.usuario.vida > 0:
            if random.random() > 0.5:
                self.usuario.recibir_puntos_habilidad(random.randint(1, 3))
            else:
                self.usuario.curar(random.randint(10, 50))
        return self.usuario.vida > 0
