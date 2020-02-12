def mattar(T_pr, P_pr, rho_pr, z, P_pc_corr):
  import numpy as np

  a1 = 0.3265; a2 = -1.0700; a3 = -0.5339; a4 = 0.01569; a5 = -0.05165; a6 = 0.5475
  a7 = -0.7361; a8 = 0.1844; a9 = 0.1056; a10 = 0.6134; a11 = 0.7210

  do = ((a1 + (a2/T_pr) + (a3/T_pr**3) +(a4/T_pr**4) + (a5/T_pr**5)) * rho_pr) + \
      (2 * ((a6 + (a7/T_pr) + (a8/T_pr**2))) * rho_pr**2) - \
      (5 * a9 * (((a7/T_pr) + (a8/T_pr**2))) * rho_pr**4) + (1 + (a11 * rho_pr**2) - (a11 * rho_pr**2)**2) \
      * ((2 * a10 * rho_pr / T_pr**3)*np.exp(-a11 * rho_pr**2))

  c_pr_analytical = (1 / P_pr) - ((0.27 / (z**2 * T_pr)) * (do / (1 + ((rho_pr / z) * do))))
  cgas_analytical = c_pr_analytical / P_pc_corr
  return(cgas_analytical)