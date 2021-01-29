import scipy.integrate as integrate
from rays import Rays
import numpy as np

class facet:
  def __init__(self, facet_cords, facet_normal):
    self.shadowing=False
    self.cords=facet_cords
    #stored as a list of numpy arrays for the vertices of the facets
    self.normal=facet_normal
    self.centroid=self.generate_centroid()
  #take vertice vectors, average
  def generate_centroid(self):
    return np.add(np.array([1,2,3]),np.array([1,2,3]),np.array([2,3,4]))/3