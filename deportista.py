class Deportista:
    _deporte: str
    _añosPracticando: int
    
    def __init__(self, deporte: str, añosPracticando: int):
        self._deporte = deporte
        self._añosPracticando = añosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte: str):
        self._deporte = deporte
        
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setAñosPracticandolo(self, añosPracticando):
        self._añosPracticando = añosPracticando