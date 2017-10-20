import sys
import random
import statistics
import time



class Chromosome:
    def __init__(self,genes,fitness):
        self.Genes = genes
        self.Fitness = fitness

class Benchmark:
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            sys.stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)
            if i < 10 or i % 10 == 9:
                print("{} {:3.2f} {:3.2f}".format(1 + i, mean, statistics.stdev(timings, mean) if i > 1 else 0))


def _generate_parent(length, geneSet, get_fitness):
    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    #genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)



def _mutate(parent,geneSet, get_fitness):
    index = random.randrange(0, len(parent.Genes))
    childGenes =  parent.Genes[:] #list(parent.Genes)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    #genes = ''.join(childGenes)
    fitness = get_fitness(childGenes)
    return Chromosome(childGenes, fitness)




def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    random.seed()
    def fnMutate(parent):
        return _mutate(parent,geneSet, get_fitness)

    def fnGenerateParent():
        return _generate_parent(targetLen, geneSet, get_fitness)
    # display(bestParent)
    # #if bestParent.Fitness >= optimalFitness: # Used by guessPasswordTest
    # #    return bestParent
    #
    # if not optimalFitness > bestParent.Fitness:
    #     return bestParent
    for improvement in _get_improvement(fnMutate, fnGenerateParent):
        display(improvement)
        if not optimalFitness > improvement.Fitness:
            return improvement


def _get_improvement(new_child, generate_parent):
    bestParent = generate_parent()
    yield bestParent

    while True:
        child = new_child(bestParent)#_mutate(bestParent, geneSet, get_fitness)
        if bestParent.Fitness > child.Fitness: ## >= Used by guessPasswordTest
           continue
        if not child.Fitness > bestParent.Fitness:
            bestParent = child
            continue
            # display(child)
        yield child
        # if not optimalFitness > child.Fitness:
        #     return child
        #
        # display(child) # only one parameter
        #
        # # if child.Fitness >= optimalFitness: ## Used by guessPasswordTest
        # #    return child

        bestParent = child

