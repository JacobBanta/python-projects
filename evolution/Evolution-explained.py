from alive_progress import alive_bar#imports a specific part of the alive_progress library(aka module)
import random as rd#imports the random library(aka module) and renames it to rd
population = []#creates a list where the population is saved to
gen = 0#keeps track of what year it is(note: the name for it was chosen for something else, but i am too lazy to fix it now)
for x in range(10):#runs the following code 1 times
    #this adds the starting population to the population list
    population.append([x, 1, gen, rd.randint(1,10), rd.randint(1,10)])#decide starting traits for reproduction and survival. It also stores lineage and generation
on = 1#sets the state for the while loop
mutation_rate = 3#decides how quickly the population can evolve
while(on == 1):#runs the main loop
    inp = input("input: ")#takes an input from a user
    if inp == "exit":#exits the program if the user types exit
        on = 0
    if inp == "step":#steps forward through time
        inp = int(input("number of steps: "))#asks how many years to step through
        if inp > 10:#if the input was more than 10(exclusively) uses progress bar type 1
            with alive_bar(inp, bar='classic') as bar:#starts the progress bar
                for x in range(inp):#runs the code the amount of times selected
                    gen += 1#adds 1 to the gen variable
                    if gen % 10 ==  0:#if the gen variable is divisible by 10, then it outputs the value of gen
                        print("gen:", gen)
                    survival_rate = []#creates new lists for tracking all of the genes in the population (note: values are added later)
                    reproduction_rate = []
                    for i in range(len(population)):#runs once for each member of population
                        reproduction_rate.append(population[i][3])#adds values of the reproductive gene to make a list of every on of them
                    for i in range(len(population)):
                        rand = rd.randint(1, max(reproduction_rate) * 2)#creates a random number between 1 and twice the highest reproductive rate
                        if population[i][3] >= rand:# if the reproductive rate is high enough, it will make baby
                            population.append([population[i][0], population[i][1] + 1, gen, rd.randint(population[i][3] - mutation_rate, population[i][3] + mutation_rate), rd.randint(population[i][4] - mutation_rate, population[i][4] + mutation_rate)])#adds a population member with their parent's genes slightly altered
                    for i in range(len(population)):
                        survival_rate.append(population[i][4])#adds values of the survival gene to make a list of every on of them
                    if (min(survival_rate) * 2) < max(survival_rate):#kills the unfit
                        dead = [index for (index, item) in enumerate(survival_rate) if item <= (2 * min(survival_rate))]
                        for j in range(len(dead)):
                            population.pop(dead[j] - j)
                        dead = []
                    bar()#adds to the progress bar
        else:#does the same thing but with progress bar type 2
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

    if inp == "list":#give some info
        print("population count:",len(population),"\ngen:",gen)
        lineage = []
        for i in range(len(population)):
            lineage.append(population[i][0])
        print("lineages:",lineage.count(0),lineage.count(1),lineage.count(2),lineage.count(3),lineage.count(4),lineage.count(5),lineage.count(6),lineage.count(7),lineage.count(8),lineage.count(9))
    if inp == "pop" or inp == "population":#give count of population
        print("population count:",len(population))
    if inp == "gen" or inp == "generation":#prints the year
        print("gen:",gen)
    if inp == "lineage" or inp == "lineages":#prints the lineages
        for i in range(len(population)):
            lineage.append(population[i][0])
        print("lineages:",lineage.count(0),lineage.count(1),lineage.count(2),lineage.count(3),lineage.count(4),lineage.count(5),lineage.count(6),lineage.count(7),lineage.count(8),lineage.count(9))
    if inp == "top" or inp == "best":#give the top traits
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
