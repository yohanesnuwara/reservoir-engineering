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

def  hall_and_yarborough(T_pr, P_pr):
  # T_pr : calculated pseudoreduced temperature
  # P_pr : calculated pseudoreduced pressure
  
  """ 
  References:
  1. Hall, K. and L. Yarborough, A new equation of state for Z-factor calculations. Oil Gas J., 1973. 71: p. 82-92
  
  2. Al-Fatlawi, O., M.M. Hossain, and J. Osborne, Determination of best possible correlation for gas compressibility 
  factor to accurately predict the initial gas reserves ingas-hydrocarbon reservoirs. International Journal of Hydrogen Energy, 
  2017. 42(2017): p. 25492 - 25508.
  
  3. Kareem, L.A., T.M. Iwalewa, and M. Al-Marhoun, New explicit correlation for the compressibility 
  factor of natural gas: linearized z-factor isotherms. Journal of Petroleum Exploration and Production Technology, 
  2016. 6(3): p. 481-492. 
 
  """  
  c0 = 0.06125*np.exp(-1.21*(1-1/T_pr)**2)
  c1 = 14.76/T_pr - 9.76/T_pr**2 + 4.58/T_pr**3
  c2 = 90.7/T_pr - 242.2/T_pr**2 + 42.4/T_pr**3
  c3 = 2.18 +2.82/T_pr  
  func = lambda y: -c0*P_pr + (y + y**2 + y**3 - y**4)/(1-y)**3 - c1*y**2 + c2*y**c3
  y0 = 0.245*np.exp(-1.2*(1-1/T_pr)**2)  
  y = fsolve(func, y0) # 0.5 => initial value
  z = float(c0*P_pr/y) 
  return(z)
