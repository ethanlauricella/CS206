
import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1.0
width = 1.0
height = 1.0

x = 0
y = 0
z = height/2

for x_pos in range(5):
    for y_pos in range(5):
        length = 1.0
        width = 1.0
        height = 1.0
        z = height/2
        for i in range(10):
            pyrosim.Send_Cube(name="Box"+str(i), pos=[x_pos, y_pos, z], size=[length, width, height])
            z+=1

            length *= .9
            width *= .9
            height *= .9


pyrosim.End()

