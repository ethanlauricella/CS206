import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.setGravity(0,0,-50)
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

backLegJointValues = np.zeros(1000)
frontLegJointValues = np.zeros(1000)

amplitudeBackLeg = -math.pi/4.0
frequencyBackLeg = 1/10.0
phaseOffsetBackLeg = 5

amplitudeFrontLeg = math.pi/4.0
frequencyFrontLeg = 1/20.0
phaseOffsetFrontLeg = 0



for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    backLegPosition = math.sin(frequencyBackLeg * i + phaseOffsetBackLeg) * amplitudeBackLeg
    frontLegPosition = math.sin(frequencyFrontLeg * i + phaseOffsetFrontLeg)* amplitudeFrontLeg

    backLegJointValues[i] = backLegPosition
    frontLegJointValues[i] = frontLegPosition
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName="Torso_BackLeg",

        controlMode=p.POSITION_CONTROL,


        targetPosition=backLegPosition,

        maxForce=500)

    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName="FrontLeg_Torso",

        controlMode=p.POSITION_CONTROL,

        targetPosition=frontLegPosition,

        maxForce=500)


    t.sleep(1./240.)

print(backLegSensorValues)
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)
np.save("data/backLegJointValues", backLegJointValues)
np.save("data/frontLegJointValues", frontLegJointValues)

p.disconnect()