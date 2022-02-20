
from simulation import SIMULATION

simulate = SIMULATION()

'''
import pybullet as p
import time as t
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math as math
import constants as c



pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

backLegJointValues = np.zeros(1000)
frontLegJointValues = np.zeros(1000)





for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

    backLegPosition = math.sin(c.frequencyBackLeg * i + c.phaseOffsetBackLeg) * c.amplitudeBackLeg
    frontLegPosition = math.sin(c.frequencyFrontLeg * i + c.phaseOffsetFrontLeg) * c.amplitudeFrontLeg

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


    t.sleep(1./480.)

print(backLegSensorValues)
np.save("data/backLegSensorValues", backLegSensorValues)
np.save("data/frontLegSensorValues", frontLegSensorValues)
np.save("data/backLegJointValues", backLegJointValues)
np.save("data/frontLegJointValues", frontLegJointValues)

p.disconnect()
'''
