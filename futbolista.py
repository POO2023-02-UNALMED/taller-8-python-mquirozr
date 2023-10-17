from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    _golesMarcados: int
    _tarjetasRojas: int
    _piernaHabil: str
    listaFutbolistas = []
    
    @classmethod
    def añadirFutbolista(cls, futbolista):
        cls.listaFutbolistas.append(futbolista)
        
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.añadirFutbolista(self)
        
    def __str__(self) -> str:
        return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"
        
    def getGolesMarcados(self):
        return self._golesMarcados
        
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
        
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
        
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    