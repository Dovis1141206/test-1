import random
import string

# 목표 문자열
TARGET = "HELLO WORLD"
POP_SIZE = 200
MUTATION_RATE = 0.01

def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + ' ') for _ in range(length))

def fitness(individual):
    return sum(individual[i] == TARGET[i] for i in range(len(TARGET)))

def crossover(parent1, parent2):
    point = random.randint(0, len(TARGET) - 1)
    return parent1[:point] + parent2[point:]

def mutate(individual):
    return ''.join(
        c if random.random() > MUTATION_RATE else random.choice(string.ascii_uppercase + ' ')
        for c in individual
    )

# 초기 개체군 생성
population = [random_string(len(TARGET)) for _ in range(POP_SIZE)]
generation = 0

while True:
    generation += 1
    # 적합도 계산
    population = sorted(population, key=fitness, reverse=True)
    best = population[0]
    print(f"Gen {generation}: {best} (fitness: {fitness(best)})")

    if best == TARGET:
        print("✅ 진화 완료!")
        break

    # 상위 20%만 선택
    survivors = population[:POP_SIZE // 5]

    # 다음 세대 생성
    new_population = []
    while len(new_population) < POP_SIZE:
        p1, p2 = random.sample(survivors, 2)
        child = crossover(p1, p2)
        child = mutate(child)
        new_population.append(child)
    population = new_population
