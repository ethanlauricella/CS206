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
        self.time = 0


    def Set_Value(self, desiredAngle, robot):
        self.time += 1

        pyrosim.Set_Motor_For_Joint(

            bodyIndex=robot,

            jointName=self.jointName,

            controlMode=p.POSITION_CONTROL,

            targetPosition=desiredAngle * c.motorJointRange * np.sin(self.time * np.pi / c.freq),

            maxForce=c.force)

    def Save_Values(self):
        np.save("Data/" + str(self.jointName) + "Motor", self.motorValues)
