import pybullet as p
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import math as math


class MOTOR:
    def __init__(self, jointName):
        MOTOR.Prepare_To_Act(self, jointName)

    def Prepare_To_Act(self, jointName):
        self.jointName = jointName
        motorValues = np.zeros(1000)
        self.motorValues = motorValues



        self.amplitude = eval("c.amplitude" + jointName)
        self.frequency = eval("c.frequency" + jointName)
        self.offset = eval("c.offset" + jointName)

    def Set_Value(self, i, robot):
        self.motorValues[i] = math.sin(self.frequency * i + self.offset) * self.amplitude

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=self.motorValues[i],

            maxForce=500)
        pass

    def Save_Values(self):
        np.save("data/" + str(self.jointName) + "Motor", self.motorValues)
