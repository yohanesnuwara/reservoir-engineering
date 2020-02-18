def solution_type_2(distance, time, poro, ct, k, rw_conv, h, mu_oil, pi, re, q, Bo):
  "Chap 6.4 Constant-Rate Solutions: Infinite Cylindrical Reservoir with Line-Source Well"

  import pandas as pd
  from scipy.special import expi
  
  eq_arr = []
  p_D_arr = []
  pressure_arr = []

  for i in range(len(distance_conv)):
    t_D = (0.0002637 * k * time) / (poro * mu_oil * ct * (distance_conv[i]**2))
    r_D = distance_conv[i] / rw
    
    if t_D > 12.5:
      # p_D can be approximated using Eq 6.28
      eq = "6.28"
      eq_arr.append(eq)

      p_D = 0.5 * (np.log(t_D) + 0.80907)
      # p_D_arr.append(float(p_D))
      
      "Calculate pressure after n hours"
      pressure = pi - ((p_D * q * Bo * mu_oil) / (0.007082 * k * h))

      p_D_arr.append(float(p_D))
      pressure_arr.append(float(pressure))   

    if t_D < 12.5:
      # p_D calculated using Eq 6.26. Find the value of integral exponent function -Ei(-x) using tabulation 
      eq = "6.26"
      eq_arr.append(eq)    

      x = 0.25 * (1 / t_D)

      if x >= 0 and x <= 0.209:
        x_new = round(x, 3)

        # "Tabulation value finder"
        index = np.where(Ei_table[:,0] == x_new)
        index = np.array((index)[0])
        index = int(index)
        minusEi = Ei_table[index, 1]

      if x > 0.209 and x <= 2.09:
        x_new = round(x, 2) 

        # "Tabulation value finder"
        index = np.where(Ei_table[:,0] == x_new)
        index = np.array((index)[0])
        index = int(index)
        minusEi = Ei_table[index, 1]

      if x > 2.09 and x <= 10.9:
        x_new = round(x, 1) 

        # "Tabulation value finder"
        index = np.where(Ei_table[:,0] == x_new)
        index = np.array((index)[0])
        index = int(index)
        minusEi = Ei_table[index, 1]

      if x > 10.9:
        # if x above 10.9, meaning Table A-1 can't be used because it's limited to only x below 10.9. so use scipy
        x_new = x
        minusEi = -expi(-x) # from scipy.expi
      
      "Calculate p_D"
      p_D = 0.5 * minusEi

      "Calculate pressure after n hours"
      pressure = pi - ((p_D * q * Bo * mu_oil) / (0.007082 * k * h))
    
      p_D_arr.append(float(p_D))
      pressure_arr.append(float(pressure))
      
      x_arr.append(float(x_new)) 
      minus_Ei_arr.append(float(minusEi))
  
  return(t_D_arr, p_D_arr, pressure_arr, eq_arr)
