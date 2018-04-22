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



class HelloWorldTests(unittest.TestCase):
    geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        print("Testing Hello World")
        target = "Hello World!"
        self.hello_world(target)


    def hello_world(self, target):
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



# Testing
if __name__ == '__main__':
    print("Running Main Tests")
    unittest.main()
