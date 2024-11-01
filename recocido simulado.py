import math
import random

# Definimos el problema del viaje del vendedor con una matriz de distancias
distancias = [[0, 2, 2, 5, 7],
              [2, 0, 4, 8, 2],
              [2, 4, 0, 1, 3],
              [5, 8, 1, 0, 2],
              [7, 2, 3, 2, 0]]

n_ciudades = len(distancias)

# Función para calcular la longitud de un recorrido
def calcular_longitud_recorrido(recorrido):
    longitud = 0
    for i in range(len(recorrido) - 1):
        longitud += distancias[recorrido[i]][recorrido[i+1]]
    longitud += distancias[recorrido[-1]][recorrido[0]]  # Regreso al punto de origen
    return longitud

# Función para generar un vecino, intercambiando dos ciudades del recorrido
def generar_vecino(recorrido):
    nuevo_recorrido = recorrido[:]
    i, j = random.sample(range(len(recorrido)), 2)  # Elegimos dos posiciones aleatorias
    nuevo_recorrido[i], nuevo_recorrido[j] = nuevo_recorrido[j], nuevo_recorrido[i]
    return nuevo_recorrido

# Función de recocido simulado
def recocido_simulado(temperatura_inicial, tasa_enfriamiento):
    # Inicialización: Generamos un recorrido inicial aleatorio
    recorrido_actual = list(range(n_ciudades))
    random.shuffle(recorrido_actual)
    longitud_actual = calcular_longitud_recorrido(recorrido_actual)
    
    # Inicializamos el mejor recorrido encontrado
    mejor_recorrido = recorrido_actual[:]
    mejor_longitud = longitud_actual

    temperatura = temperatura_inicial

    while temperatura > 1:
        # Generamos un vecino (una pequeña variación del recorrido actual)
        vecino = generar_vecino(recorrido_actual)
        longitud_vecino = calcular_longitud_recorrido(vecino)
        
        # Calculamos la diferencia de energía (distancia)
        delta_longitud = longitud_vecino - longitud_actual
        
        # Si el vecino es mejor, lo aceptamos
        if delta_longitud < 0:
            recorrido_actual = vecino
            longitud_actual = longitud_vecino
        # Si el vecino es peor, lo aceptamos con una probabilidad que depende de la temperatura
        else:
            probabilidad = math.exp(-delta_longitud / temperatura)
            if random.random() < probabilidad:
                recorrido_actual = vecino
                longitud_actual = longitud_vecino
        
        # Actualizamos el mejor recorrido encontrado
        if longitud_actual < mejor_longitud:
            mejor_recorrido = recorrido_actual[:]
            mejor_longitud = longitud_actual
        
        # Enfriamos la temperatura
        temperatura *= tasa_enfriamiento

    return mejor_recorrido, mejor_longitud

# Parámetros del recocido simulado
temperatura_inicial = 10000
tasa_enfriamiento = 0.995

# Ejecutamos el algoritmo
mejor_recorrido, mejor_longitud = recocido_simulado(temperatura_inicial, tasa_enfriamiento)

print("Mejor recorrido encontrado:", mejor_recorrido)
print("Longitud del mejor recorrido:", mejor_longitud)
