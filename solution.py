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
        self.weights1 = np.random.rand(c.numSensorNeurons, c.numHiddenNeurons) * 2 - 1
        self.weights2 = np.random.rand(c.numHiddenNeurons, c.numMotorNeurons) * 2 - 1

        if exists(c.file):

            f = open(c.file, "r")

            fitness = f.readline()

            for i in range(c.numSensorNeurons):
                for j in range(c.numHiddenNeurons):
                    self.weights1[i][j] = f.readline()

            for x in range(c.numHiddenNeurons):
                for y in range(c.numMotorNeurons):
                    self.weights2[x][y] = f.readline()

            f.close()



    def Set_ID(self, Id):
        self.myID = Id

    def Start_Simulation(self, directOrGui):
        self.Create_world()
        self.Create_body()
        self.Create_brain()

        if c.comp == 0:
            os.system("start /B python3 simulate.py " + directOrGui + " " + str(self.myID))
        else:
            os.system("python3 simulate.py " + directOrGui + " " + str(self.myID) + " &")

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            t.sleep(0.01)

        f = open("fitness" + str(self.myID) + ".txt", "r")
        t.sleep(0.01)
        self.fitness = float(f.readline())
        t.sleep(0.01)
        f.close()
        os.remove("fitness" + str(self.myID) + ".txt")


    def Mutate(self):

        randomRow1 = random.randint(0, c.numSensorNeurons - 1)
        randomColumn1 = random.randint(0, c.numHiddenNeurons - 1)
        self.weights1[randomRow1, randomColumn1] = random.random() * 2 - 1

        randomRow2 = random.randint(0, c.numHiddenNeurons - 1)
        randomColumn2 = random.randint(0, c.numMotorNeurons - 1)
        self.weights2[randomRow2, randomColumn2] = random.random() * 2 - 1

    def Create_world(self):
        pyrosim.Start_SDF("World.sdf")
        pyrosim.End()

    def Set_Id(self, Id):
        self.Id = Id

    def Create_body(self):
        pyrosim.Start_URDF("Body.urdf")

        sim_height = 1.  # height off the ground

        body_height = .55 / 2.  # thickness in z direction
        body_length = 1.2  # length in x direction
        body_width = .5  # width in y direction

        pyrosim.Send_Cube(name="Torso", pos=[0., 0., sim_height], size=[body_length, body_width, body_height])

        # Parameters

        leg_spreadX = body_length / 4.0 + .1 / 2.0  # how far apart along the torso
        leg_spreadY = .3  # how far from torso outwards
        leg_height = sim_height + .3 / 2.0  # Height off ground from torso

        leg_x = .25 / 2.0  # thickness of leg in x direction
        leg_y = .23 / 2.0  # thickness of leg in y direction

        for i in range(1, 5):
            pyrosim.Send_Cube(name="Leg" + str(i) + "A", pos=[-.3 / 2.0, .0, -.5 / 2.0], size=[leg_x, leg_y, 1 / 2.0],
                              rpy=[0, 1.57 / 2.0, .0])
            pyrosim.Send_Cube(name="Leg" + str(i) + "B", pos=[0.2 / 2.0, 0., -.33 / 2.0],
                              size=[leg_x - .05 / 2.0, leg_y - .01 / 2.0, 1 / 2.0], rpy=[0, -1.57 / 2.0, .0])

            pyrosim.Send_Joint(name="Leg" + str(i) + "A_Leg" + str(i) + "B", parent="Leg" + str(i) + "A",
                               child="Leg" + str(i) + "B", type="revolute",
                               position=[-0.52 / 2.0, 0., -.92 / 2.0], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="Torso_Leg1A", parent="Torso", child="Leg1A", type="revolute",
                           position=[leg_spreadX, leg_spreadY, leg_height], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="Torso_Leg2A", parent="Torso", child="Leg2A", type="revolute",
                           position=[-leg_spreadX, leg_spreadY, leg_height], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="Torso_Leg3A", parent="Torso", child="Leg3A", type="revolute",
                           position=[leg_spreadX, -leg_spreadY, leg_height], jointAxis="0 1 0")

        pyrosim.Send_Joint(name="Torso_Leg4A", parent="Torso", child="Leg4A", type="revolute",
                           position=[-leg_spreadX, -leg_spreadY, leg_height], jointAxis="0 1 0")

        # pyrosim.Send_Joint(name="Torso_Rod1", parent="Torso", child="Rod1", type="revolute",
        #                    position=[.5, 0., 2.25], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Rod1", pos=[0., .0, 0.3], size=[0.3, .3, .6])

        # pyrosim.Send_Joint(name="Rod1_Rod2", parent="Rod1", child="Rod2", type="revolute",
        #                   position=[0.,0.,.6], jointAxis="0 1 0")
        # pyrosim.Send_Cube(name="Rod2", pos=[0.3, .0, 0], size=[.6, .3, .3])

        for i in range(1, 5):
            pyrosim.Send_Joint(name="Leg" + str(i) + "B_Foot" + str(i) + "", parent="Leg" + str(i) + "B",
                               child="Foot" + str(i) + "", type="fixed",
                               position=[.55 / 2.0, 0., -.68 / 2.0], jointAxis="0 0 0")
            pyrosim.Send_Sphere(name="Foot" + str(i) + "", pos=[.0, .0, .0], size=[.16 / 2.0])

        pyrosim.End()

    def Create_brain(self):

        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        sensorNum = 0
        hiddenNum = c.numSensorNeurons
        motorNum = c.numSensorNeurons + c.numHiddenNeurons

        #linkNames = ["Torso", "Leg1A", "Leg1B"]
        #jointNames =


        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Torso")
        sensorNum += 1

        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg1A")
        sensorNum += 1
        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg1B")
        sensorNum += 1

        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Leg1A_Leg1B")
        motorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Torso_Leg1A")
        motorNum += 1

        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg2A")
        sensorNum += 1
        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg2B")
        sensorNum += 1

        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Leg2A_Leg2B")
        motorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Torso_Leg2A")
        motorNum += 1

        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg3A")
        sensorNum += 1
        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg3B")
        sensorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Leg3A_Leg3B")
        motorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Torso_Leg3A")
        motorNum += 1

        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg4A")
        sensorNum += 1
        pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Leg4B")
        sensorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Leg4A_Leg4B")
        motorNum += 1
        pyrosim.Send_Motor_Neuron(name=motorNum, jointName="Torso_Leg4A")
        motorNum += 1

        for j in range(c.numHiddenNeurons):
            pyrosim.Send_Hidden_Neuron(name=hiddenNum)
            hiddenNum += 1

        # pyrosim.Send_Sensor_Neuron(name=9, linkName="Rod1")
        # pyrosim.Send_Sensor_Neuron(name=10, linkName="Rod2")
        # pyrosim.Send_Motor_Neuron(name=19, jointName="Torso_Rod1")
        # pyrosim.Send_Motor_Neuron(name=20, jointName="Rod1_Rod2")

        for i in range(1, 5):
            pyrosim.Send_Sensor_Neuron(name=sensorNum, linkName="Foot" + str(i))
            sensorNum += 1

        for currentRow in range(c.numSensorNeurons):
            for hidden in range(c.numHiddenNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=hidden + c.numSensorNeurons,
                                     weight=self.weights1[currentRow][hidden])

        for hidden2 in range(c.numHiddenNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName=hidden2 + c.numSensorNeurons,
                                     targetNeuronName=currentColumn + c.numSensorNeurons + c.numHiddenNeurons,
                                     weight=self.weights2[hidden2][currentColumn])

        pyrosim.End()

