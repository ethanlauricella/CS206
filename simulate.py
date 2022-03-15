
from simulation import SIMULATION
import sys
import os



directOrGUI = sys.argv[1]

simulate = SIMULATION(directOrGUI)

simulate.Run()

simulate.Save_Sensor()
simulate.Save_Motor()
simulate.Get_Fitness()