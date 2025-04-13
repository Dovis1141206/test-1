import random
import string

TARGET = "Hello, World!"
POPULATION_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000

def random_char():
    return random.choice(string.printable)

def random_individual():
    return ''.join(random_char() for _ in range(len(TARGET)))

def fitness(individual):
    return sum(1 for i, c in enumerate(individual) if c == TARGET[i])

def mutate(individual):
    return ''.join(
        c if random.random() > MUTATION_RATE else random_char()
        for c in individual
    )

def crossover(parent1, parent2):
    pivot = random.randint(0, len(TARGET)-1)
    return parent1[:pivot] + parent2[pivot:]

# 초기 인구 생성
population = [random_individual() for _ in range(POPULATION_SIZE)]

for generation in range(GENERATIONS):
    # 적합도 기준 정렬
    population = sorted(population, key=fitness, reverse=True)
    
    if fitness(population[0]) == len(TARGET):
        print(f"\n🎉 세대 {generation}에서 성공!")
        print(f"문자열: {population[0]}")
        break

    next_generation = population[:10]  # 상위 10개는 무조건 다음 세대

    while len(next_generation) < POPULATION_SIZE:
        parents = random.choices(population[:50], k=2)
        child = crossover(parents[0], parents[1])
        child = mutate(child)
        next_generation.append(child)

    population = next_generation

    if generation % 50 == 0 or generation == 0:
        print(f"[세대 {generation}] 최고 적합도: {fitness(population[0])} → {population[0]}")

else:
    print("\n😥 목표 문자열에 도달하지 못했어요.")
