from solution import SOLUTION
import constants as c
import copy
import os


class HILL_CLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):

        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness


    def Print(self):
        print("\n Parent Fitness " + str(self.parent.fitness) + " Child Fitness " + str(self.child.fitness))

    def Show_Best(self):
        self.Select()
        self.parent.Evaluate("GUI")