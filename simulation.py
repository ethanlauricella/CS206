import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math
import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:
    # Constructor
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -50)

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        self.robot.Prepare_To_Act()
        for i in range(1000):

            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act()
            '''

            self.backLegJointValues[i] = backLegPosition
            self.frontLegJointValues[i] = frontLegPosition

            '''
            t.sleep(1. / 480.)

    def Save_Sensor(self):
        self.robot.Save_Sensor()
    def Save_Motor(self):
        self.robot.Save_Motor()



    def __del__(self):
        p.disconnect()
