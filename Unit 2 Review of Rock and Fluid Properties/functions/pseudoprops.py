def pseudoprops(temp, pressure, sg, x_h2s, x_co2):
  import numpy as np
  temp = temp + 459.67 # convert to Rankine

  # calculate pseudocritical properties (Sutton, valid for 0.57<sg<1.68)
  P_pc = 756.8 - (131.07 * sg) - (3.6 * sg**2)
  T_pc = 169.2 + (349.50 * sg) - (74 * sg**2) # in Rankine

  # calculate adjustment to pseudocritical properties for sour gas (Wiechert-Aziz, valid for x_co2<0.544 and x_h2s<0.738)
  e = (120 * (((x_h2s + x_co2)**0.9) - ((x_h2s + x_co2)**1.6))) + (15 * (x_h2s**0.5 - x_h2s**4))
  T_pc_corr = T_pc - e # corrected T_pc
  P_pc_corr = (P_pc * T_pc_corr) / (T_pc - x_h2s * e * (1-x_h2s))

  # calculate pseudoreduced properties
  P_pr = pressure / P_pc_corr
  T_pr = temp / T_pc_corr

  return(P_pr, T_pr)
