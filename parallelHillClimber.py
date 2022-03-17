from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        self.nextAvalibleID = 0
        self.parents = {}
        self.children = {}
        for bot in range(c.populationSize):
            self.parents[bot] = SOLUTION(self.nextAvalibleID)
            self.nextAvalibleID += 1
        print(self.parents)


    def Evolve(self):
        for bot in range(c.populationSize):
            self.parents[bot].Evaluate("GUI")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        #self.Mutate()
        #for key in self.children:
        #    self.children[key].Evaluate("DIRECT")
        #self.Print()
        #self.Select()

    def Spawn(self):
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_Id(self.nextAvalibleID)
            self.nextAvalibleID += 1


    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):

        if self.parent.fitness > self.child.fitness:
            self.parent.fitness = self.child.fitness


    def Print(self):
        #print("\n Parent Fitness " + str(self.parent.fitness) + " Child Fitness " + str(self.child.fitness))
        pass

    def Show_Best(self):
        self.Select()
        self.parent.Evaluate("GUI")