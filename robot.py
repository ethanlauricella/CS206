import pybullet as p
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        ROBOT.Prepare_To_Sense(self)
        ROBOT.Prepare_To_Act(self)

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, i):
        for j in self.sensors:
            self.sensors[j].Get_Value(i)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self,i):
        for j in self.motors:
            self.motors[j].Set_Value(i,self.robotId)

    def Save_Sensor(self):
        for j in self.sensors:
            self.sensors[j].Save_Values()

    def Save_Motor(self):
        for j in self.motors:
            self.motors[j].Save_Values()