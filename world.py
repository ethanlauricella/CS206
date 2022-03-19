import pybullet_data
import pybullet as p
import time as t


class WORLD:
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.planeId = p.loadURDF("plane.urdf")
        t.sleep(1. / 30.)
        p.loadSDF("world.sdf")
