def fetkovich_initial_encroachable_water(pi, ct, r_R, r_aq, h_aq, poro, theta):
  "calculate initial encroachable water"
  # r_R: reservoir size (radius of cylindrical-assumed reservoir), in ft
  # r_aq: aquifer size, in ft
  # theta: for full circle cylindrical, theta=360. if half-circle, theta=180
  
  import numpy as np
  
  Wei = (pi * ct * np.pi * ((r_aq**2) - (r_R**2)) * h_aq * poro * theta) / (5.61458 * 360)
  return(Wei)

def fetkovich_productivity_index_flow(perm, h_aq, mu_w, r_aq, r_R, theta):
  "calculate productivity index for condition of FLOW FROM THE AQUIFER"
  # mu_w: water viscosity
  
  import numpy as np
  
  J = (0.007082 * perm * h_aq * theta) / ((mu_w * (np.log(r_aq / r_R) - 0.75) * 360))
  return(J)

def fetkovich_productivity_index_noflow(perm, h, mu_w, r_aq, r_R, theta):
  "calculate productivity index for condition of NO FLOW / CONSTANT PRESSURE AT THE OUTER BOUNDARY"
  # mu_w: water viscosity
  
  import numpy as np
  
  J = (0.007082 * perm * h_aq * theta) / ((mu_w * (np.log(r_aq / r_R)) * 360))
  return(J)
