import numpy as np
from stl import mesh
import math

from math import *

import copy

asteroid_stl = mesh.Mesh.from_file('Steins.stl')

a=copy.deepcopy(asteroid_stl.normals)
asteroid_stl.rotate([0.0, 0.5, 0.0], math.radians(100))
print("111111111")
asteroid_stl.update_normals()
b=a==asteroid_stl.normals
print(b.all())
def rotationMatrix(rx, ry, rz):
    # Convert from degrees to radians
    rx = radians(rx)
    ry = radians(ry)
    rz = radians(rz)

    Rx = np.array([[1,         0,          0],
                [0,         cos(rx),    -sin(rx)],
                [0,         sin(rx),    cos(rx)]])

    Ry = np.array([[cos(ry),   0,          sin(ry)],
                [0,         1,          0],
                [-sin(ry),  0,          cos(ry)]])

    Rz = np.array([[cos(rz),   -sin(rz),   0],
                [sin(rz),   cos(rz),    0],
                [0,         0,          1]])

    return Rx.dot(Ry.dot(Rz))

rot_x=100
rot_y=0
rot_z=0

data = np.zeros(len(asteroid_stl.vectors), dtype=mesh.Mesh.dtype)
data['vectors'] = copy.deepcopy(asteroid_stl.vectors).dot(rotationMatrix(rot_x, rot_y, rot_z))

# Create and save a mesh with the new vectors
newMesh = mesh.Mesh(data, remove_empty_areas=False)
# print(newMesh.vectors)
newMesh.save("object.stl")