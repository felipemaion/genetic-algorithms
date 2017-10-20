import string
import random
import datetime
import unittest

import genetic


def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
    if expected == actual)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(''.join(candidate.Genes), candidate.Fitness, timeDiff))



class GuessPasswordTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.geneset) for _ in range(length))
        self.guess_password(target)

    def test_Hello_World(self):
        print("Testing Hello World")
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)

    def guess_password(self, target):
        geneset = string.punctuation + " " + string.ascii_uppercase + string.ascii_lowercase
        starttime = datetime.datetime.now()
        print("GeneSet:", geneset)
        #target = "Hello Fucking World!!"

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            display(candidate, starttime)

        optimalFitness = len(target)


        best = genetic.get_best(fnGetFitness, len(target), optimalFitness,
                                self.geneset, fnDisplay)


        self.assertEqual(''.join(best.Genes), target)
        #genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)



# Testing
if __name__ == '__main__':
    print("Running Main Tests")
    unittest.main()
