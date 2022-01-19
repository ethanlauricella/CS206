import pybullet as p
import time as t
import pybullet_data

p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")

physicsClient = p.connect(p.GUI)
p.loadSDF("box.sdf")

for i in range(10000):
    p.stepSimulation()
    t.sleep(1./240.)
    #print(i)

p.disconnect()