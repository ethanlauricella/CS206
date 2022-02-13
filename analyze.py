
import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

plt.plot(backLegSensorValues, linewidth=4, label='BackLeg')
plt.plot(frontLegSensorValues, linewidth=2, label='FrontLeg')
plt.legend()
plt.show()