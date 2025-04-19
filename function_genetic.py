import random
import math

# 적합도 함수: f(x) = x * sin(10πx) + 1.0
def fitness(x):
    return x * math.sin(10 * math.pi * x) + 1.0

# 유전 알고리즘 파라미터
POPULATION_SIZE = 20
GENERATIONS = 100
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.9
BOUNDS = (0.0, 1.0)

# 초기 개체군 생성
def generate_population():
    return [random.uniform(*BOUNDS) for _ in range(POPULATION_SIZE)]

# 토너먼트 선택
def selection(population):
    k = 3
    selected = random.sample(population, k)
    return max(selected, key=fitness)

# 실수 기반 평균 교차
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        alpha = random.random()
        child1 = alpha * parent1 + (1 - alpha) * parent2
        child2 = alpha * parent2 + (1 - alpha) * parent1
        return child1, child2
    else:
        return parent1, parent2

# 돌연변이
def mutate(x):
    if random.random() < MUTATION_RATE:
        x += random.gauss(0, 0.1)
        x = max(min(x, BOUNDS[1]), BOUNDS[0])  # 경계 체크
    return x

# 메인 알고리즘
population = generate_population()
for gen in range(GENERATIONS):
    new_population = []
    while len(new_population) < POPULATION_SIZE:
        p1 = selection(population)
        p2 = selection(population)
        c1, c2 = crossover(p1, p2)
        new_population.append(mutate(c1))
        if len(new_population) < POPULATION_SIZE:
            new_population.append(mutate(c2))
    population = new_population

    best = max(population, key=fitness)
    print(f"Generation {gen+1}: Best x = {best:.5f}, f(x) = {fitness(best):.5f}")
