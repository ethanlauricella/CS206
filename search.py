#!/usr/bin/env python

from parallelHillClimber import PARALLEL_HILL_CLIMBER

f = open("FitnessGraph.txt", "w")
f.close()

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()

