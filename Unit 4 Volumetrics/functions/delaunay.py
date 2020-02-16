"Delaunay triangulation for tricontouring method"

### After running this function, must be followed by code of: tricontouring.py (not a function, just copy that code)

def triangulation(x, y, z, smoothness):

  # x, y, z: coordinates, depth data to be contoured
  # smoothness: value > 3 is already smooth, controls how smooth will the contour be

  import numpy as np
  import math
  from scipy.interpolate import griddata
  
  # Now create the Triangulation.
  # (Creating a Triangulation without specifying the triangles results in the
  # Delaunay triangulation of the points.)
  triang = tri.Triangulation(x, y)

  #-----------------------------------------------------------------------------
  # Refine data
  #-----------------------------------------------------------------------------
  refiner = tri.UniformTriRefiner(triang)
  tri_refi, z_test_refi = refiner.refine_field(z, smoothness)
  
  return(triang, refiner, tri_refi, z_test_refi)
 
