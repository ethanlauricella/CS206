import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math
import constants as c
import os
import random as random
from os.path import exists

class SOLUTION:

    def __init__(self, Id):
        self.myID = Id
        self.weights = np.zeros((c.numSensorNeurons, c.numMotorNeurons))
        file_exists = exists("../data/Final.txt")

        if file_exists and self.myID == 0:
            f = open("../data/Final.txt", "r")
            fitness = f.readline()
            for i in range(c.numSensorNeurons):
                for j in range(c.numMotorNeurons):
                    self.weights[i][j] = float(f.readline())
            f.close()
        else:
            for i in range(c.numSensorNeurons):
                for j in range(c.numMotorNeurons):
                    self.weights[i][j] = np.random.rand() * 2 - 1
            pass

    def Set_ID(self, Id):
        self.myID = Id

    def Start_Simulation(self, directOrGui):
        self.Create_world()
        self.Create_body()
        self.Create_brain()
        #os.system("start /B C:/Users/Ethan/anaconda3/python.exe simulate.py " + directOrGui + " " + str(self.myID))
        os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " &")
        pass

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            t.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.readline())
        f.close()
        t.sleep(1. / 10.)
        os.remove("fitness" + str(self.myID) + ".txt")

    def Evaluate(self, directOrGui):
        pass

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons - 1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_world(self):
        pyrosim.Start_SDF("World.sdf")

        # pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()

    def Set_Id(self, Id):
        self.Id = Id

    def Create_body(self):

        pyrosim.Start_URDF("Body.urdf")

        pyrosim.Send_Cube(name="Torso", pos=[0., 0., 2.], size=[1.7, 1.0, .5])

        pyrosim.Send_Joint(name="Torso_Leg1A", parent="Torso", child="Leg1A", type="revolute",
                           position=[0.5, .6, 2.], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="Leg1A", pos=[0., .0, -0.5], size=[0.3, .3, 1.])

        pyrosim.Send_Joint(name="Leg1A_Leg1B", parent="Leg1A", child="Leg1B", type="revolute",
                           position=[0., 0., -0.7], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Leg1B", pos=[0., 0., -.5], size=[0.3, 0.3, .7])


        pyrosim.Send_Joint(name="Torso_Leg2A", parent="Torso", child="Leg2A", type="revolute",
                           position=[-0.5, .6, 2.], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="Leg2A", pos=[0., 0., -0.5], size=[0.3, .3, 1.])

        pyrosim.Send_Joint(name="Leg2A_Leg2B", parent="Leg2A", child="Leg2B", type="revolute",
                           position=[0., 0., -0.7], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Leg2B", pos=[0., 0., -.5], size=[0.3, 0.3, .7])


        pyrosim.Send_Joint(name="Torso_Leg3A", parent="Torso", child="Leg3A", type="revolute",
                           position=[0.5, -.6, 2.], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="Leg3A", pos=[0., 0., -.5], size=[0.3, 0.3, 1.])

        pyrosim.Send_Joint(name="Leg3A_Leg3B", parent="Leg3A", child="Leg3B", type="revolute",
                           position=[0., 0, -0.7], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Leg3B", pos=[0., 0., -.5], size=[0.3, 0.3, .7])


        pyrosim.Send_Joint(name="Torso_Leg4A", parent="Torso", child="Leg4A", type="revolute",
                           position=[-0.5, -.6, 2.], jointAxis="1 1 0")
        pyrosim.Send_Cube(name="Leg4A", pos=[0., 0., -.5], size=[0.3, .3, 1.])

        pyrosim.Send_Joint(name="Leg4A_Leg4B", parent="Leg4A", child="Leg4B", type="revolute",
                           position=[0., 0., -0.7], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Leg4B", pos=[0., 0., -.5], size=[0.3, 0.3, .7])


        pyrosim.Send_Joint(name="Torso_Rod1", parent="Torso", child="Rod1", type="revolute",
                           position=[.5, 0., 2.25], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Rod1", pos=[0., .0, 0.3], size=[0.3, .3, .6])

        pyrosim.Send_Joint(name="Rod1_Rod2", parent="Rod1", child="Rod2", type="revolute",
                           position=[0.,0.,.6], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="Rod2", pos=[0.3, .0, 0], size=[.6, .3, .3])



        pyrosim.End()

    def Create_brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")

        pyrosim.Send_Sensor_Neuron(name=1, linkName="Leg1A")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="Leg1B")

        pyrosim.Send_Motor_Neuron(name=11, jointName="Leg1A_Leg1B")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_Leg1A")

        pyrosim.Send_Sensor_Neuron(name=3, linkName="Leg2A")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="Leg2B")

        pyrosim.Send_Motor_Neuron(name=13, jointName="Leg2A_Leg2B")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_Leg2A")

        pyrosim.Send_Sensor_Neuron(name=5, linkName="Leg3A")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="Leg3B")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Leg3A_Leg3B")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Torso_Leg3A")

        pyrosim.Send_Sensor_Neuron(name=7, linkName="Leg4A")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="Leg4B")
        pyrosim.Send_Motor_Neuron(name=17, jointName="Leg4A_Leg4B")
        pyrosim.Send_Motor_Neuron(name=18, jointName="Torso_Leg4A")

        pyrosim.Send_Sensor_Neuron(name=9, linkName="Rod1")
        pyrosim.Send_Sensor_Neuron(name=10, linkName="Rod2")
        pyrosim.Send_Motor_Neuron(name=19, jointName="Torso_Rod1")
        pyrosim.Send_Motor_Neuron(name=20, jointName="Rod1_Rod2")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        pyrosim.End()
