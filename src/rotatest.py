from stl import mesh
import numpy as np 
import math

stl1 = mesh.Mesh.from_file('Steins100.stl')
print(stl1.v0[69])

#stl1.rotate([0.5,0,0],math.radians(90))
#print(stl1.v0[69])

stl1.rotate([1,0,0],math.radians(90))
print(stl1.v0[69])