import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math
import constants as c
import os
import random as random

class SOLUTION:

    def __init__(self):
        self.weights = np.zeros((3,2))
        for i in range(3):
            for j in range(2):
                self.weights[i][j] = np.random.rand() * 2 - 1
        pass

    def Evaluate(self, directOrGui):
        self.Create_world()
        self.Create_body()
        self.Create_brain()

        os.system("C:/Users/Ethan/anaconda3/python.exe simulate.py " + directOrGui)

        f = open("fitness.txt", "r")
        self.fitness = f.readline()
        f.close()
        pass

    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow,randomColumn] = random.random() * 2 - 1


    def Create_world(self):
        pyrosim.Start_SDF("world.sdf")
        length = 1.0
        width = 1.0
        height = 1.0

        x = 0
        y = 0
        z = height / 2

        # pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()

    def Create_body(self):

        pyrosim.Start_URDF("body.urdf")

        length = 1
        width = 1
        height = 1

        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0.5, .5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="FrontLeg", child="Torso", type="revolute",
                           position=[1.0, 0.5, 1.0])
        pyrosim.Send_Cube(name="Torso", pos=[0.5, 0.0, 0.5], size=[length, width, height])

        pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0.0, -0.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[1.0, 0.0, 0.0])
        pyrosim.End()

    def Create_brain(self):

        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=5.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=5.0)

        pyrosim.End()

