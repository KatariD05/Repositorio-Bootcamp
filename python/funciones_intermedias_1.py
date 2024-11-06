# 1. Actualizar valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0]=6
print(matriz)

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0].update({"nombre" :  "Enrique Martin Morales"})
print(cantantes)

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0].update({"latitud": 9.9355431})
print(coordenadas)

# 2. Iterar a través de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
def iterarDiccionario(cantantes):
    for i in cantantes:
        claves = i.keys()
        lista_claves = list(claves)
        print(f"{lista_claves[0]} - {i['nombre']} , {lista_claves[1]} - {i['pais']} ")

iterarDiccionario(cantantes)

# 3.Obtener valores de una lista de diccionarios
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
def iterarDiccionario2(llave, lista):
    for cantantes in lista:
            print(cantantes[llave])

iterarDiccionario2("nombre", cantantes)
iterarDiccionario2("pais", cantantes)

# 4. Iterar a través de un diccionario con valores de lista

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirInformacion(costa_rica):
    for llave, valores in costa_rica.items():
        print(f"{len(valores)} {llave}")
        for valor in valores:
            print(f"{valor}")

imprimirInformacion(costa_rica)

