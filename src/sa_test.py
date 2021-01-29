import numpy as np
from stl import mesh

stl1 = mesh.Mesh.from_file('Steins.stl')
stl2 = mesh.Mesh.from_file('Steins100.stl')
stl3 = mesh.Mesh.from_file('Steins750.stl')
stl4 = mesh.Mesh.from_file('Steins1500.stl')

print(stl1.areas.sum())
print(stl2.areas.sum())
print(stl3.areas.sum())
print(stl4.areas.sum())

print(stl1.get_mass_properties())