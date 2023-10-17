class Persona:
    _nombre: str
    _edad: int
    _altura: str
    _sexo: str   

    def __init__(self, nombre: str, edad: int, altura: str, sexo:str):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre: int):
        self._nombre = nombre    
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad: int):
        self._edad = edad
        
    def getAltura(self):
        return self._altura
    
    def setAltura(self, altura: int):
        self._altura = altura
        
    def getSexo(self):
        return self._sexo
    
    def setSexo(self, sexo: int):
        self._sexo = sexo