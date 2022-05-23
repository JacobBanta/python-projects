from alive_progress import alive_bar
import random as rd
population = []
gen = 0
for x in range(10):

    population.append([x, 1, gen, rd.randint(1,10), rd.randint(1,10)])#decide starting traits for reproduction and survival. It also stores lineage and generation
on = 1
mutation_rate = 3
while(on == 1):
    inp = input("input: ")
    if inp == "exit":
        on = 0
    if inp == "step":
        inp = int(input("number of steps: "))
        if inp > 10:
            with alive_bar(inp, bar='classic') as bar:
                for x in range(inp):
                    gen += 1
                    if gen % 10 ==  0:
                        print("gen:", gen)
                    survival_rate = []
                    reproduction_rate = []
                    for i in range(len(population)):
                        reproduction_rate.append(population[i][3])
                    for i in range(len(population)):
                        rand = rd.randint(1, max(reproduction_rate) * 2)
                        if population[i][3] >= rand:#reproduction
    #explanation of below VVV             continue lineage | lineage generation | gen | mutate reproductive gene                                                       | mutate survival gene
                            population.append([population[i][0], population[i][1] + 1, gen, rd.randint(population[i][3] - mutation_rate, population[i][3] + mutation_rate), rd.randint(population[i][4] - mutation_rate, population[i][4] + mutation_rate)])
                    for i in range(len(population)):
                        survival_rate.append(population[i][4])
                    if (min(survival_rate) * 2) < max(survival_rate):
                        dead = [index for (index, item) in enumerate(survival_rate) if item <= (2 * min(survival_rate))]
                        for j in range(len(dead)):
                            population.pop(dead[j] - j)
                        dead = []
                    bar()
        else:
            for x in range(inp):
                with alive_bar(len(population), bar='classic')as bar:
                    gen += 1
                    if gen % 10 ==  0:
                        print("gen:", gen)
                    survival_rate = []
                    reproduction_rate = []
                    for i in range(len(population)):
                        reproduction_rate.append(population[i][3])
                    for i in range(len(population)):
                        bar()
                        rand = rd.randint(1, max(reproduction_rate) * 2)
                        if population[i][3] >= rand:
                            population.append([population[i][0], population[i][1] + 1, gen, rd.randint(population[i][3] - mutation_rate, population[i][3] + mutation_rate), rd.randint(population[i][4] - mutation_rate, population[i][4] + mutation_rate)])
                    for i in range(len(population)):
                        survival_rate.append(population[i][4])
                    if (min(survival_rate) * 2) < max(survival_rate):
                        dead = [index for (index, item) in enumerate(survival_rate) if item <= (2 * min(survival_rate))]
                        for j in range(len(dead)):
                            population.pop(dead[j] - j)
                        dead = []

    if inp == "list":
        print("population count:",len(population),"\ngen:",gen)
        lineage = []
        for i in range(len(population)):
            lineage.append(population[i][0])
        print("lineages:",lineage.count(0),lineage.count(1),lineage.count(2),lineage.count(3),lineage.count(4),lineage.count(5),lineage.count(6),lineage.count(7),lineage.count(8),lineage.count(9))
    if inp == "pop" or inp == "population":
        print("population count:",len(population))
    if inp == "gen" or inp == "generation":
        print("gen:",gen)
    if inp == "lineage" or inp == "lineages":
        for i in range(len(population)):
            lineage.append(population[i][0])
        print("lineages:",lineage.count(0),lineage.count(1),lineage.count(2),lineage.count(3),lineage.count(4),lineage.count(5),lineage.count(6),lineage.count(7),lineage.count(8),lineage.count(9))
    if inp == "top" or inp == "best":
        topr = []
        tops = []
        age = []
        for i in range(len(population)):
            topr.append(population[i][3])
            tops.append(population[i][4])
            age.append(population[i][2])
        print("highest reproduction rate:",max(topr))
        print("highest survival:",max(tops))
        print("oldest:", gen - min(age))
