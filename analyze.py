
import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

backLegJointValues = numpy.load("data/backLegJointValues.npy")
frontLegJointValues = numpy.load("data/frontLegJointValues.npy")

#plt.plot(backLegSensorValues, linewidth=4, label='BackLeg')
#plt.plot(frontLegSensorValues, linewidth=2, label='FrontLeg')

plt.plot(backLegJointValues, linewidth=2, label='BackLeg')
plt.plot(frontLegJointValues, linewidth=2, label='FrontLeg')

plt.legend()
plt.show()