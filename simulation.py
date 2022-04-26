import pybullet as p
import time as t
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math
import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    # Constructor
    def __init__(self, directOrGUI, solutionID):
        self.solutionID = solutionID
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setGravity(0, 0, c.grav)

        self.world = WORLD()
        self.robot = ROBOT(self.solutionID)

    def Run(self):
        for i in range(c.iterations):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()

            if self.directOrGUI == "GUI":
                t.sleep(0.01)

    def Save_Sensor(self):
        self.robot.Save_Sensor()

    def Save_Motor(self):
        self.robot.Save_Motor()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()
