import pyrosim.pyrosim as pyrosim

def Create_world():
    pyrosim.Start_SDF("world.sdf")
    length = 1.0
    width = 1.0
    height = 1.0

    x = 0
    y = 0
    z = height / 2

    #pyrosim.Send_Cube(name="Box", pos=[x, y, z], size=[length, width, height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="Link0", pos=[0.5, 0.5, .5], size=[length, width, height])
    pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[1.0, 0.5, 1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0.5, 0.0, 0.5], size=[length, width, height])

    pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[1.0, 0.0, 0.0])
    pyrosim.Send_Cube(name="Link2", pos=[0.5, 0.0, -0.5], size=[length, width, height])


    pyrosim.End()


Create_world()
Create_Robot()
