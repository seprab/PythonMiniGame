# Python Text-Based RPG Mini-Game

Este espacio lo destinare al desarrollo de un mini juego de tipo text-based RPG. Para hacerlo sencillo pienso basarme en el juego de 'Buriedbornes" de la play store. Siendo asi, el juego consistira en lo siguiente:

## Descripción

El juego consiste en una torre de pisos infinitos que se generan aleatoriamente. En cada piso, el usuario se encontrará con enemigos aleatorios de diferentes caracteristicas a los que se deberá enfrentar. Perder un pelea reiniciará el juego y ganarla le proporcionará al usuario puntos de habilidad y el avance al siguiente piso.

El juego:
  * Permitirá al usuario crear un personaje que será jugable mientras la instancia del juego duré abierta o termine el juego.
  * Todo jugador nuevo tendrá las siguientes estadisticas:
      *Fuerza: Fuerza bruta y Defensa bruta.
      *Inteligencia: Poder magico y Defensa magica.
      *Precision: Intensificador de poder fisico
      *Vida: Cantidad de vida del usuario - [estadistica de 0 a 100]
  * Las estadisticas subirán de nivel según la decisión del usuario a medida que avance por cada piso de la torre al adquirir puntos e habilidad.
  * Todo jugador tendra en su inventario:
      *Espada: Cuyo daño consiste en la cantidad de fuerza bruta.
      *Vara magica: Cuyo daño consiste en la cantidad de inteligencia.
      *Arco: Cuyo daño consiste en la precision del usuario y el numero de flechas disponibles.
  * De manera aleatoria, el usuario recibirá daño en cada pelea y se curará al vencer enemigos.
  
  
## La estrtuctura del juego en código es:

  *Clase Entidad:
      *[Propiedad] Vida
      *[Propiedad] Defensa fisica
      *[Propiedad] Defensa magica
      *[Propiedad] Poder fisica
      *[Propiedad] Poder magica
      
      *[Metodo] Dañar (int cantidad) -> ModificarVida (cantidad) + Eventos adicionales
      *[Metodo] Curar (int cantidad) -> ModificarVida (cantidad) + Eventos adicionales
      *[Metodo] ModificarVida (int cantidad) -> Suma la cantidad de vida recibida a la propiedad Vida
      *[Metodo] Atacar (Entidad, int magia, int fisico) -> Metodo recibirAtaque de la otra entidad
      *[Metodo] RecibirAtaque (int magia, int fisico) -> Calcular daño para llamar el metodo Dañar(), el daño debería calcularse en base a la defensa
      
      
      *[Clase Heredada] Clase Heroe:
          *[Propiedad] Precisión
          *[Propiedad] Numero flechas
          
          *[Metodo] UsarAtaque (ref Ataque) -> con espada, con vara o (flechas -> reducir flechas [si es igual a 0 returnar false]). -> Atacar
          *[Metodo] ModificarNoFlechas (int cantidad) -> Sumar si encuentra o reducir si las usa
          *[Metodo] UsarPuntoHabilidad() -> Metodo que permite subir la propiedad magica, fisica y precisión
         
      *[Clase Heredada] 
          *[Metodo morir] EventoMorir -> Asignado aleatoriamente
          *[Metodo] regalar_flechas -> Heroe.MofificarNoFlechas(Rand(1-10))
          *[Metodo] regalar_puntosHabilidad -> Heroe.UsarPuntoHabilidad(Rand(1-3))
         
    *Clase Enfrentamiento:
      Debe encargarse de enfrentar el usuario y un mounstro hasta que alguno muera
      
      
    *Clase ControladorJuego:
      Debe encargarse de llevar el control de los pisos, enfrentamientos, inicio y final del juego






