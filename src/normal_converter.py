import numpy
from stl import mesh
import os

dir_name=os.getcwd()
dir_name=dir_name[0:len(dir_name)-3]+"models/"

asteroid_stl = mesh.Mesh.from_file(dir_name+'Steins.stl')

normal_vectors=asteroid_stl.normals

numpy.save("toutatis_normals", normal_vectors)