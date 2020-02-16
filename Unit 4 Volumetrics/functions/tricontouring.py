#-----------------------------------------------------------------------------
# Plot the triangulation and the high-res iso-contours
#-----------------------------------------------------------------------------

### This is a code, not a function. Is preceded by triangulation using delaunay.py function. After running it, copy this code to plot the result. 

import matplotlib.tri as tri
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# INPUTS: 
# triang, refiner, tri_refi, z_test_refi: results from delaunay.py function
# level: controls how dense the contours will be, 10 is common, higher level = denser contour
# label: controls the appearance of labeling contour value, 3 is common, higher label = more frequent the contour label will be, 1 = per contour is labeled
  
plt.figure(figsize=(20, 10))
plt.gca().set_aspect('equal')
plt.triplot(triang, lw=0.5, color='white')

levels = np.linspace(min(z)+10, max(z)-10, level)  ##contour range, divided by 10 levels
cmap = cm.get_cmap(name='terrain', lut=None)
fig = plt.tricontourf(tri_refi, z_test_refi, levels=levels, cmap=cmap)
fig = plt.tricontour(tri_refi, z_test_refi, levels=levels,
                 colors=['0.25', '0.5', '0.5', '0.5', '0.5'],
                 linewidths=[1.0, 0.5, 0.5, 0.5, 0.5])
plt.plot(x, y, 'ko', ms=3) # plot the well points
plt.clabel(fig, fig.levels[::label], inline=1, fontsize=10) # give labels for contours, fig.levels[::x] controls the frequency of labels
                                                          # lesser ::x, more populated by labels
plt.title("Structure Map using Triangulation Method", pad=10, size=20)

plt.show()
