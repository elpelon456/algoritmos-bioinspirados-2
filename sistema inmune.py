import random
import math

# Función Rastrigin para evaluar soluciones
def funcion_rastrigin(solucion):
    x, y = solucion
    return 20 + x**2 + y**2 - 10 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))

# Función para generar una nueva solución mutada (aleatoria dentro de un rango)
def mutar(solucion, rango_mutacion):
    x, y = solucion
    nuevo_x = x + random.uniform(-rango_mutacion, rango_mutacion)
    nuevo_y = y + random.uniform(-rango_mutacion, rango_mutacion)
    return [nuevo_x, nuevo_y]

# Función para inicializar una población de soluciones (anticuerpos)
def inicializar_poblacion(tamano_poblacion, rango_inicial):
    poblacion = []
    for _ in range(tamano_poblacion):
        solucion = [random.uniform(-rango_inicial, rango_inicial), random.uniform(-rango_inicial, rango_inicial)]
        poblacion.append(solucion)
    return poblacion

# Función para seleccionar las mejores soluciones de la población
def seleccionar_mejores(poblacion, num_seleccionados):
    poblacion_ordenada = sorted(poblacion, key=funcion_rastrigin)
    return poblacion_ordenada[:num_seleccionados]

# Algoritmo de Sistema Inmune Artificial para optimización de funciones
def sistema_inmune_artificial(tamano_poblacion, num_generaciones, tasa_mutacion, num_seleccionados, rango_mutacion, rango_inicial):
    # Inicialización de la población de soluciones
    poblacion = inicializar_poblacion(tamano_poblacion, rango_inicial)
    
    mejor_solucion = None
    mejor_valor = float('inf')

    for generacion in range(num_generaciones):
        # Seleccionamos las mejores soluciones
        mejores_anticuerpos = seleccionar_mejores(poblacion, num_seleccionados)
        
        # Actualizamos la mejor solución encontrada
        valor_mejor = funcion_rastrigin(mejores_anticuerpos[0])
        if valor_mejor < mejor_valor:
            mejor_solucion = mejores_anticuerpos[0]
            mejor_valor = valor_mejor
        
        # Generamos la nueva población clonando y mutando las mejores soluciones
        nueva_poblacion = []
        for anticuerpo in mejores_anticuerpos:
            # Clonamos y mutamos según la tasa de mutación
            for _ in range(int(tamano_poblacion / num_seleccionados)):
                if random.random() < tasa_mutacion:
                    nuevo_anticuerpo = mutar(anticuerpo, rango_mutacion)
                else:
                    nuevo_anticuerpo = anticuerpo[:]
                nueva_poblacion.append(nuevo_anticuerpo)
        
        # La nueva población sustituye a la anterior
        poblacion = nueva_poblacion
        
        # Imprimir el progreso de cada generación
        print(f"Generación {generacion+1}: Mejor valor = {mejor_valor}")

    return mejor_solucion, mejor_valor

# Parámetros del sistema inmune artificial
tamano_poblacion = 50
num_generaciones = 100
tasa_mutacion = 0.5
num_seleccionados = 10
rango_mutacion = 0.1
rango_inicial = 5.12  # Rango común para la función Rastrigin

# Ejecutamos el algoritmo
mejor_solucion, mejor_valor = sistema_inmune_artificial(tamano_poblacion, num_generaciones, tasa_mutacion, num_seleccionados, rango_mutacion, rango_inicial)

print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la mejor solución:", mejor_valor)
