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

    def __init__(self, Id):
        self.myID = Id
        self.weights = np.zeros((c.numSensorNeurons, c.numMotorNeurons))
        for i in range(3):
            for j in range(2):
                self.weights[i][j] = np.random.rand() * 2 - 1
        pass

    def Set_ID(self, Id):
        self.myID = Id

    def Start_Simulation(self, directOrGui):
        self.Create_world()
        self.Create_body()
        self.Create_brain()
        os.system("start /B C:/Users/Ethan/anaconda3/python.exe simulate.py " + directOrGui + " " + str(self.myID))
        pass

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            t.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.readline())
        f.close()
        t.sleep(1./60.)
        os.remove("fitness" + str(self.myID) + ".txt")

    def Evaluate(self, directOrGui):
        pass

    def Mutate(self):
        randomRow = random.randint(0, c.numSensorNeurons - 1)
        randomColumn = random.randint(0, c.numMotorNeurons -1)
        self.weights[randomRow, randomColumn] = random.random() * 2 - 1

    def Create_world(self):
        pyrosim.Start_SDF("World.sdf")
        length = 1.0
        width = 1.0
        height = 1.0

        x = 0
        y = 0
        z = height / 2

        # pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

        pyrosim.End()

    def Set_Id(self, Id):
        self.Id = Id

    def Create_body(self):

        pyrosim.Start_URDF("Body.urdf")

        length = 1
        width = 1
        height = 1
        pyrosim.Send_Cube(name="Torso", pos=[0.,0.,1.], size=[length, width, height])

        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute",
                           position=[0, .5, 1.], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.,.5,0.], size=[0.2, 1., 0.2])

        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute",
                           position=[0., -.5, 1.], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLeg", pos=[0.,-.5,0.], size=[0.2, 1., 0.2])

        pyrosim.Send_Joint(name="Torso_LeftLeg", parent="Torso", child="LeftLeg", type="revolute",
                           position=[0.5, 0., 1.], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[0.5,0.,0.], size=[1., 0.2, 0.2])

        pyrosim.Send_Joint(name="Torso_RightLeg", parent="Torso", child="RightLeg", type="revolute",
                           position=[-.5, 0., 1.], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[-.5,0.,0.], size=[1., 0.2, 0.2])

        # Bottom Legs
        pyrosim.Send_Joint(name="Torso_FrontLeg2", parent="FrontLeg", child="FrontLeg2", type="revolute",
                           position=[0., 1, 0.], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        pyrosim.Send_Joint(name="Torso_BackLeg2", parent="BackLeg", child="BackLeg2", type="revolute",
                           position=[0., -1., 0.], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="LeftLeg", child="LeftLeg2", type="revolute",
                           position=[1., 0., 0.], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])

        pyrosim.Send_Joint(name="Torso_RightLeg2", parent="RightLeg", child="RightLeg2", type="revolute",
                           position=[-1.,0, 0.], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLeg2", pos=[0., 0., -.5], size=[0.2, 0.2, 1.])



        pyrosim.End()

    def Create_brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")

        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg2")

        pyrosim.Send_Sensor_Neuron(name=3, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="FrontLeg2")

        pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftLeg")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLeg2")

        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightLeg")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLeg2")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_RightLeg")

        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_FrontLeg2")
        pyrosim.Send_Motor_Neuron(name=14, jointName="Torso_BackLeg2")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_LeftLeg2")
        pyrosim.Send_Motor_Neuron(name=16, jointName="Torso_RightLeg2")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn + c.numSensorNeurons,
                                     weight=self.weights[currentRow][currentColumn])

        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.0)
        # pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)

        # pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=5.0)
        # pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=5.0)



        pyrosim.End()
