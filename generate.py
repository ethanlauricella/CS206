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


def Generate_body():

    pyrosim.Start_URDF("body.urdf")

    length = 1
    width = 1
    height = 1

    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0.5, .5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_FrontLeg", parent="FrontLeg", child="Torso", type="revolute", position=[1.0, 0.5, 1.0])
    pyrosim.Send_Cube(name="Torso", pos=[0.5, 0.0, 0.5], size=[length, width, height])

    pyrosim.Send_Cube(name="BackLeg", pos=[0.5, 0.0, -0.5], size=[length, width, height])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1.0, 0.0, 0.0])
    pyrosim.End()

def Generate_brain():

    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=3, weight=-1.0)
    pyrosim.Send_Synapse(sourceNeuronName=1, targetNeuronName=3, weight=1.0)

    pyrosim.Send_Synapse(sourceNeuronName=0, targetNeuronName=4, weight=5.0)
    pyrosim.Send_Synapse(sourceNeuronName=2, targetNeuronName=4, weight=5.0)

    pyrosim.End()


Create_world()
Generate_body()
Generate_brain()
