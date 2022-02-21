
import numpy as numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load("data/BackLegSensor.npy")
frontLegSensorValues = numpy.load("data/FrontLegSensor.npy")

backLegJointValues = numpy.load("data/BackLegJoint.npy")
frontLegJointValues = numpy.load("data/FrontLegJoint.npy")

#plt.plot(backLegSensorValues, linewidth=4, label='BackLeg')
#plt.plot(frontLegSensorValues, linewidth=2, label='FrontLeg')

plt.plot(backLegJointValues, linewidth=2, label='BackLeg')
plt.plot(frontLegJointValues, linewidth=2, label='FrontLeg')

plt.legend()
plt.show()