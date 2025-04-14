import random

# 파라미터
POP_SIZE = 6
GENE_LENGTH = 5  # 0~31을 표현하기 위해 5비트 필요
GENERATIONS = 20
MUTATION_RATE = 0.1

def fitness(x):
    return x ** 2

def decode(chromosome):
    return int(chromosome, 2)

def encode(x):
    return format(x, f'0{GENE_LENGTH}b')

def select(population):
    # 룰렛휠 선택 (확률적으로 적합도가 높은 염색체 선택)
    total_fitness = sum(fitness(decode(c)) for c in population)
    pick = random.uniform(0, total_fitness)
    current = 0
    for chromosome in population:
        current += fitness(decode(chromosome))
        if current >= pick:
            return chromosome
    return population[-1]

def crossover(parent1, parent2):
    point = random.randint(1, GENE_LENGTH - 1)
    return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]

def mutate(chromosome):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, GENE_LENGTH - 1)
        mutated = list(chromosome)
        mutated[index] = '1' if chromosome[index] == '0' else '0'
        return ''.join(mutated)
    return chromosome

# 초기 집단 생성
population = [encode(random.randint(0, 31)) for _ in range(POP_SIZE)]

# 세대 반복
for generation in range(GENERATIONS):
    population = sorted(population, key=lambda c: fitness(decode(c)), reverse=True)
    print(f"세대 {generation}: 최고 해 = {decode(population[0])}, 적합도 = {fitness(decode(population[0]))}")
    
    new_population = population[:2]  # elitism: 상위 2개는 그대로 유지

    while len(new_population) < POP_SIZE:
        parent1 = select(population)
        parent2 = select(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.append(mutate(child1))
        if len(new_population) < POP_SIZE:
            new_population.append(mutate(child2))

    population = new_population
