class Ataque:
    nombre: str
    ataque_fisica: float
    ataque_magica: float
    requiere_flechas: bool

    def __init__(self, _nombre: str, _ataque_fisica: float, _ataque_magica: float, _requiere_flechas: bool):
        self.nombre = _nombre
        self.ataque_fisica = _ataque_fisica
        self.ataque_magica = _ataque_magica
        self.requiere_flechas = _requiere_flechas
        pass

    def __str__(self):
        intro = f"{self.nombre}\t poder físico:{self.ataque_fisica}\t poder mágico:{self.ataque_magica}"
        return intro
