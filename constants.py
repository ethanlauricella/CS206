import math as math
import numpy as np

iterations = 4000
grav = -20.0

windows = 0
linux = 1
comp = 0

numberOfGenerations = 2
populationSize = 3

motorJointRange = 1.

numSensorNeurons = 13
numMotorNeurons = 8

force = 150
# sin function CPP
freq = 250

# Generate.py, in Generate_Brain()
sensors = np.arange(numSensorNeurons)
motors = np.arange(numSensorNeurons,numMotorNeurons)

