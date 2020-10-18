from typing import List
from Clases.Entidades import Entidad
from Clases.Heroe import Heroe
from Clases.Ataque import Ataque


class Mounstro(Entidad):

    nivel: int

    def __init__(self, _nombre: str, _ataques: List[Ataque], _def_magica: float, _def_fisica: float, _atk_fisco: float,
                 _atk_magico):
        Entidad.__init__(self, _nombre, _ataques)
        self.defensa_fisica = _def_fisica
        self.defensa_magica = _def_magica
        self.ataque_fisica = _atk_fisco
        self.ataque_magica = _atk_magico
        self.nivel = 0
        pass

    def atacar(self, objetivo: Heroe, ataque: Ataque):
        Entidad.atacar(self, objetivo, ataque)
        poder_magico_total = (ataque.ataque_magica * self.ataque_magica) + self.nivel
        poder_fisico_total = (ataque.ataque_fisica * self.ataque_fisica) + self.nivel
        objetivo.recibir_ataque(poder_magico_total, poder_fisico_total)
        return True

    def al_morir(self):
        print(f"{self.nombre} ha muerto en batalla")
