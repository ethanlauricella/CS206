from solution import SOLUTION
import constants as c
import copy
import os
import glob, os
import time as t


class PARALLEL_HILL_CLIMBER:

    def __init__(self):

        for f in glob.glob("*.nndf"):
            os.remove(f)

        self.nextAvalibleID = 0
        self.parents = {}
        for bot in range(c.populationSize):
            self.parents[bot] = SOLUTION(self.nextAvalibleID)
            self.nextAvalibleID += 1

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        print("\n")
        self.Print()
        print("\n")
        self.Select()

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_Id(self.nextAvalibleID)
            self.nextAvalibleID += 1

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

    def Select(self):
        for key in self.parents:
            if self.parents[key].fitness < self.children[key].fitness:
                self.parents[key].fitness = self.children[key].fitness

    def Print(self):
        best = -2
        total = 0
        for key in self.parents:
            print("Parent Fitness " + str(self.parents[key].fitness) + " Child Fitness " + str(
                self.children[key].fitness))

            #if self.parents[key].fitness > best:
            #    best_key = key
            #    best = self.parents[key].fitness

            # Add average value of bests parents
            total += self.parents[key].fitness


        f = open("FitnessGraph.txt", "a")
        t.sleep(0.01)
        f.write(str(total/ c.populationSize) + "\n")
        t.sleep(0.01)
        f.close()



    def Show_Best(self):
        best = -2
        for key in self.parents:
            if self.parents[key].fitness > best:
                best_key = key
                best = self.parents[key].fitness
        print(self.parents[best_key].fitness)
        #self.parents[best_key].Start_Simulation("DIRECT")
        self.parents[best_key].Start_Simulation("GUI")


        #f = open("../Data/Final.txt", "w")
        f = open("Final.txt", "w")

        f.write(str(self.parents[best_key].fitness) + "\n")
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                f.write(str(self.parents[best_key].weights[i][j]) + "\n")
        f.close()


    def Evaluate(self, solutions):
        for bot in range(c.populationSize):
            solutions[bot].Start_Simulation("DIRECT")
        for bot in range(c.populationSize):
            solutions[bot].Wait_For_Simulation_To_End()

