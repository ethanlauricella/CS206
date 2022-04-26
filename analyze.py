
import numpy as numpy
import matplotlib.pyplot as plt

foot1 = numpy.load("Data/Foot1Sensor.npy")
foot2 = numpy.load("Data/Foot2Sensor.npy")

foot3 = numpy.load("Data/Foot3Sensor.npy")
foot4 = numpy.load("Data/Foot4Sensor.npy")

#plt.plot(backLegSensorValues, linewidth=4, label='BackLeg')
#plt.plot(frontLegSensorValues, linewidth=2, label='FrontLeg')

x = numpy.arange(0,2000,1)

for i in range(2000):
    if (foot1[i] == -1):
        foot1[i] = 0
    if (foot2[i] == -1):
        foot2[i] = 0
    if (foot3[i] == -1):
        foot3[i] = 0
    if (foot4[i] == -1):
        foot4[i] = 0


plt.scatter(x, foot3*10,s=1.8,alpha=.6, label='Front Foot Right')
plt.scatter(x, foot1*9,s=1.8,alpha=.6, label='Front Foot Left')
plt.scatter(x, foot4*8,s=1.8,alpha=.6, label='Back Foot Right')
plt.scatter(x, foot2*7,s=1.8,alpha=.6, label='Back Foot Left')
plt.legend()
plt.show()