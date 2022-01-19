import pybullet as p
import time as t
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")


for i in range(10000):
    p.stepSimulation()
    t.sleep(1./240.)
    #print(i)

p.disconnect()