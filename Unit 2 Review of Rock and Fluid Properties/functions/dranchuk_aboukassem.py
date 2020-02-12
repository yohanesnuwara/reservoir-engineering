def dranchuk(T_pr, P_pr):
  # T_pr : calculated pseudoreduced temperature
  # P_pr : calculated pseudoreduced pressure   
  from scipy.optimize import fsolve # non-linear solver
  import numpy as np

  a1 = 0.3265; a2 = -1.0700; a3 = -0.5339; a4 = 0.01569; a5 = -0.05165; a6 = 0.5475
  a7 = -0.7361; a8 = 0.1844; a9 = 0.1056; a10 = 0.6134; a11 = 0.7210

  def f(y):
    rho_pr, z = y
    c1 = a1 + (a2/T_pr) + (a3/(T_pr**3))+ (a4/(T_pr**4))+ (a5/(T_pr**5))
    c2 = a6 + (a7/T_pr) + (a8/(T_pr**2))
    c3 = a9*((a7/T_pr) + (a8/(T_pr**2)))
    c4 = (a10)*(1+(a11*(rho_pr**2)))*((rho_pr**2)/(T_pr**3))*(np.exp(-a11*(rho_pr**2)))

    f1 = z + (c3*(rho_pr**5)) - (c2*(rho_pr**2)) - (c1*(rho_pr**1)) - c4 - 1
    f2 = rho_pr - ((0.27 * P_pr) / (z * T_pr))
    return[f1, f2]

  solve = fsolve(f, [1, 1]) # initial guess
  return(solve[0], solve[1])
