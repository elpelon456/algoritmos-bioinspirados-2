import random

# Parámetros del algoritmo
TAMANIO_POBLACION = 20
TAMANIO_CROMOSOMA = 8
NUMERO_GENERACIONES = 20
PROBABILIDAD_CRUCE = 32
PROBABILIDAD_MUTACION = 87

# Función de fitness
def calcular_fitness(individuo):
    return sum(individuo)  # Ejemplo simple: la suma de los genes

# Crear un individuo aleatorio
def crear_individuo():
    return [random.randint(0, 1) for _ in range(TAMANIO_CROMOSOMA)]

# Crear una población inicial
def crear_poblacion():
    return [crear_individuo() for _ in range(TAMANIO_POBLACION)]

# Selección por torneo
def seleccion(poblacion):
    seleccionados = []
    for _ in range(TAMANIO_POBLACION):
        i, j = random.sample(range(TAMANIO_POBLACION), 2)
        if calcular_fitness(poblacion[i]) > calcular_fitness(poblacion[j]):
            seleccionados.append(poblacion[i])
        else:
            seleccionados.append(poblacion[j])
    return seleccionados

# Cruce de dos padres
def cruce(padre1, padre2):
    if random.random() < PROBABILIDAD_CRUCE:
        punto_cruce = random.randint(1, TAMANIO_CROMOSOMA - 1)
        hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
        hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
        return hijo1, hijo2
    else:
        return padre1, padre2

# Mutación de un individuo
def mutacion(individuo):
    for i in range(TAMANIO_CROMOSOMA):
        if random.random() < PROBABILIDAD_MUTACION:
            individuo[i] = 1 - individuo[i]

# Algoritmo genético
def algoritmo_genetico():
    poblacion = crear_poblacion()

    for generacion in range(NUMERO_GENERACIONES):
        poblacion = seleccion(poblacion)
        nueva_poblacion = []

        # Aplicar cruce y mutación
        for i in range(0, TAMANIO_POBLACION, 2):
            padre1 = poblacion[i]
            padre2 = poblacion[i + 1]
            hijo1, hijo2 = cruce(padre1, padre2)
            mutacion(hijo1)
            mutacion(hijo2)
            nueva_poblacion.append(hijo1)
            nueva_poblacion.append(hijo2)

        poblacion = nueva_poblacion
        mejor_fitness = max([calcular_fitness(ind) for ind in poblacion])
        print(f"Generación {generacion + 1}: Mejor Fitness = {mejor_fitness}")

# Ejecutar el algoritmo
algoritmo_genetico()
