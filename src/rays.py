import numpy
from stl import mesh

class Rays:
  def __init__(self, stl_scale):
    print("rays class init")
    self.stl_scale=stl_scale
    self.rays_array=[]
    self.np_asteroid_stl = mesh.Mesh.from_file('Steins350.stl')
    self.np_asteroid_stl.x*=self.stl_scale
    self.np_asteroid_stl.y*=self.stl_scale
    self.np_asteroid_stl.z*=self.stl_scale
    self.number_of_rays=len(self.np_asteroid_stl.vectors)
    self.position=[-2.226970408619044*(0.897/2.677), 1.412027223728939*(0.897/2.677), 4.614171488645494*0.1*(0.897/2.677)]
  def generate_centroids(self):
    temp=[0,0,0]
    temp2=[]
    for i in range(self.number_of_rays):
        for j in range(3):
            temp[0]+=self.np_asteroid_stl.vectors[i][j][0]/3
            temp[1]+=self.np_asteroid_stl.vectors[i][j][1]/3
            temp[2]+=self.np_asteroid_stl.vectors[i][j][2]/3
        temp2.append(temp)
        temp=[0,0,0]
    return temp2

  def unit(self, vector):
    vector=numpy.array(vector)
    return vector/numpy.linalg.norm(vector)
    
  def generate_all_rays(self):
    #2-d array of length number of centroids, and stores the parametric eqn of the line for the centroids: [[a,b,c,x1,y1,z1]...]
    position=numpy.array(self.position)*149598073
    self.centroids=self.generate_centroids()+position
    for i in range(self.number_of_rays):
        n=numpy.concatenate((self.unit(self.centroids[i]),self.centroids[i]), axis=0)
        self.rays_array.append(n)
    return self.rays_array
