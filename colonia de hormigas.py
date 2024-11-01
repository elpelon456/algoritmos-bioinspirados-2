import random

# Definimos el problema del viaje del vendedor con una matriz de distancias
distancias = [[0, 2, 2, 5, 7],
              [2, 0, 8, 8, 2],
              [2, 4, 0, 1, 3],
              [5, 8, 1, 0, 2],
              [7, 2, 3, 2, 0]]

n_ciudades = len(distancias)
n_hormigas = 6
n_iteraciones = 10
alpha = 1  # Importancia de la feromona
beta = 5   # Importancia de la visibilidad
evaporacion = 0.5  # Tasa de evaporación de la feromona
Q = 100  # Constante para actualizar la feromona

# Inicialización de las feromonas
feromonas = [[1 for _ in range(n_ciudades)] for _ in range(n_ciudades)]

# Función para calcular la visibilidad como el inverso de la distancia
def calcular_visibilidad():
    visibilidad = [[0 for _ in range(n_ciudades)] for _ in range(n_ciudades)]
    for i in range(n_ciudades):
        for j in range(n_ciudades):
            if distancias[i][j] > 0:
                visibilidad[i][j] = 1 / distancias[i][j]
            else:
                visibilidad[i][j] = 0
    return visibilidad

visibilidad = calcular_visibilidad()

# Función para calcular la probabilidad de elegir la siguiente ciudad
def elegir_siguiente_ciudad(ciudad_actual, ciudades_no_visitadas, feromonas, visibilidad):
    feromonas_actuales = [feromonas[ciudad_actual][i] for i in ciudades_no_visitadas]
    visibilidad_actual = [visibilidad[ciudad_actual][i] for i in ciudades_no_visitadas]
    
    # Calcular la probabilidad según las feromonas y la visibilidad
    suma_probabilidades = sum((fer ** alpha) * (vis ** beta) for fer, vis in zip(feromonas_actuales, visibilidad_actual))
    probabilidades = [(fer ** alpha) * (vis ** beta) / suma_probabilidades for fer, vis in zip(feromonas_actuales, visibilidad_actual)]
    
    # Seleccionar la siguiente ciudad según las probabilidades
    return random.choices(ciudades_no_visitadas, weights=probabilidades)[0]

# Función para calcular la longitud de un recorrido
def calcular_longitud_recorrido(recorrido):
    longitud = 0
    for i in range(len(recorrido) - 1):
        longitud += distancias[recorrido[i]][recorrido[i+1]]
    longitud += distancias[recorrido[-1]][recorrido[0]]  # Regreso al punto de origen
    return longitud

# Algoritmo principal de la colonia de hormigas
mejor_recorrido = None
mejor_longitud = float('inf')

for iteracion in range(n_iteraciones):
    recorridos = []
    longitudes = []
    
    for hormiga in range(n_hormigas):
        ciudad_inicial = random.randint(0, n_ciudades - 1)
        recorrido = [ciudad_inicial]
        ciudades_no_visitadas = list(range(n_ciudades))
        ciudades_no_visitadas.remove(ciudad_inicial)
        
        while ciudades_no_visitadas:
            siguiente_ciudad = elegir_siguiente_ciudad(recorrido[-1], ciudades_no_visitadas, feromonas, visibilidad)
            recorrido.append(siguiente_ciudad)
            ciudades_no_visitadas.remove(siguiente_ciudad)
        
        longitud_recorrido = calcular_longitud_recorrido(recorrido)
        recorridos.append(recorrido)
        longitudes.append(longitud_recorrido)
        
        if longitud_recorrido < mejor_longitud:
            mejor_recorrido = recorrido
            mejor_longitud = longitud_recorrido

    # Actualización de las feromonas
    for i in range(n_ciudades):
        for j in range(n_ciudades):
            feromonas[i][j] *= (1 - evaporacion)
    
    for recorrido, longitud_recorrido in zip(recorridos, longitudes):
        for i in range(len(recorrido) - 1):
            feromonas[recorrido[i]][recorrido[i+1]] += Q / longitud_recorrido
        feromonas[recorrido[-1]][recorrido[0]] += Q / longitud_recorrido  # Retorno al punto de origen

    print(f"Iteración {iteracion+1}: Mejor longitud de recorrido = {mejor_longitud}")

print("Mejor recorrido encontrado:", mejor_recorrido)
print("Longitud del mejor recorrido:", mejor_longitud)
