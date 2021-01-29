from rays import Rays
import numpy as np
import math
from tqdm import tqdm
import scipy as sp 

class ThermalMap:
  #thermal snapshot per time step
  def __init__(self, stl_scale):
    print("thermal map class init")
    self.rays_obj=Rays(stl_scale)
    self.position = self.rays_obj.position
    self.copy_vectors=self.rays_obj.np_asteroid_stl.vectors
    self.normals=None
  def eliminate_bad_facets(self):
    distance = self.position
    indices_to_remove=[]
    for i in range(self.rays_obj.number_of_rays):
      if np.dot(distance, self.rays_obj.np_asteroid_stl.normals[i])>0:
        indices_to_remove.append(i)
    return indices_to_remove
  
  #shadowing code
  def shadowing(self):
    distance=np.array(self.position)*149598073
    indices_to_remove=self.eliminate_bad_facets()
    rays_generated=self.rays_obj.generate_all_rays()
    non_shadowed_array_indices=[]
    for i in range(self.rays_obj.number_of_rays):
      ray_temp=[]
      for j in range(self.rays_obj.number_of_rays):
        if j not in indices_to_remove and j not in non_shadowed_array_indices:
          p1=self.rays_obj.np_asteroid_stl.vectors[j][0]+distance
          p2=self.rays_obj.np_asteroid_stl.vectors[j][1]+distance
          p3=self.rays_obj.np_asteroid_stl.vectors[j][2]+distance
          q1=rays_generated[i][:3]*1000+rays_generated[i][3:]
          q2=rays_generated[i][:3]*-1000+rays_generated[i][3:]
          if self.SignedVolume(q1,p1,p2,p3)*self.SignedVolume(q2,p1,p2,p3)<0 and np.sign(self.SignedVolume(q1,q2,p1,p2))==np.sign(self.SignedVolume(q1,q2,p2,p3))==np.sign(self.SignedVolume(q1,q2,p3,p1)):
            ray_temp.append(j)
      distances=[]
      for ray in ray_temp:
        distances.append(np.linalg.norm(self.rays_obj.centroids[ray]))
      try:
        non_shadowed_array_indices.append(ray_temp[distances.index(min(distances))])
      except:
        pass
    return non_shadowed_array_indices
#p1,p2,p3 triangle; q1,q2 points on the line far away in both direction
    #If SignedVolume(q1,p1,p2,p3) and SignedVolume(q2,p1,p2,p3) have different signs AND SignedVolume(q1,q2,p1,p2), SignedVolume(q1,q2,p2,p3) and SignedVolume(q1,q2,p3,p1) have the same sign, then there is an intersection
  def SignedVolume(self,a,b,c,d):
    return (1.0/6.0)*np.dot(np.cross(np.subtract(b,a),np.subtract(c,a)),np.subtract(d,a))

  def facets_temps(self):
    pass

  def orient(self):
    v = [-0.0059690746,-0.0163998975,-0.9998476952]
    itheta = math.acos(-0.9998476952)
    axis = np.cross(v,[0,0,1])
    self.rays_obj.np_asteroid_stl.rotate(axis,itheta)
    self.rays_obj.np_asteroid_stl.update_normals()

  def rotation(self,timesteps):
    v = [0.0059690746, 0.0163998975, 0.9998476952]
    self.rays_obj.np_asteroid_stl.rotate(v,math.radians(360/timesteps))
    self.rays_obj.np_asteroid_stl.update_normals()

  def phi(self, timesteps):
    lenpos = np.linalg.norm(self.position)
    self.orient()
    facetlist = []
    for f in tqdm(range(len(self.rays_obj.np_asteroid_stl.vectors))):
      philist = []
      for t in range(timesteps):
        n = self.rays_obj.np_asteroid_stl.normals[f]
        lennorm = np.linalg.norm(n)
        philist.append(abs(np.dot(self.position,n)/(lenpos*lennorm)))
        self.rotation(timesteps)
      facetlist.append(philist)
    return facetlist




