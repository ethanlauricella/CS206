import math as math
import numpy as np



numberOfGenerations = 2
populationSize = 2

motorJointRange = 3.0

numSensorNeurons = 13
numMotorNeurons = 8

force = 1000
# sin function CPP
freq = 100

# Generate.py, in Generate_Brain()
sensors = np.arange(numSensorNeurons)
motors = np.arange(numSensorNeurons,numMotorNeurons)

