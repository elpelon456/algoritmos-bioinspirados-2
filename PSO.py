import numpy as np

# Parámetros de la función de Rastrigin
def rastrigin(position):
    return 10 * len(position) + sum(x**2 - 10 * np.cos(2 * np.pi * x) for x in position)

# Clase que representa una partícula
class Particle:
    def __init__(self, bounds):
        self.position = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
        self.velocity = np.random.uniform(-1, 1, len(bounds))
        self.best_position = np.copy(self.position)
        self.best_score = float('inf')
    
    def update_personal_best(self, objective_function):
        score = objective_function(self.position)
        if score < self.best_score:
            self.best_score = score
            self.best_position = np.copy(self.position)

# Función principal de PSO
def particle_swarm_optimization(objective_function, bounds, num_particles=30, max_iter=100, w=0.5, c1=1, c2=2):
    particles = [Particle(bounds) for _ in range(num_particles)]
    global_best_position = None
    global_best_score = float('inf')
    
    for iteration in range(max_iter):
        for particle in particles:
            # Actualizar la mejor posición de la partícula
            particle.update_personal_best(objective_function)
            
            # Actualizar la mejor posición global
            if particle.best_score < global_best_score:
                global_best_score = particle.best_score
                global_best_position = np.copy(particle.best_position)
        
        # Actualizar velocidad y posición de cada partícula
        for particle in particles:
            inertia = w * particle.velocity
            cognitive = c1 * np.random.rand() * (particle.best_position - particle.position)
            social = c2 * np.random.rand() * (global_best_position - particle.position)
            particle.velocity = inertia + cognitive + social
            particle.position += particle.velocity
            
            # Limitar las posiciones de la partícula dentro de los límites
            for i in range(len(bounds)):
                if particle.position[i] < bounds[i][0]:
                    particle.position[i] = bounds[i][0]
                elif particle.position[i] > bounds[i][1]:
                    particle.position[i] = bounds[i][1]
        
        print(f"Iteración {iteration+1}/{max_iter}, mejor puntuación global: {global_best_score}")
    
    return global_best_position, global_best_score

# Definir los límites de búsqueda para cada dimensión
bounds = [(-5.12, 5.12) for _ in range(2)]  # Aquí usamos 2 dimensiones

# Ejecutar el PSO
best_position, best_score = particle_swarm_optimization(rastrigin, bounds)
print(f"Mejor posición: {best_position}")
print(f"Mejor puntuación (mínimo encontrado): {best_score}")
