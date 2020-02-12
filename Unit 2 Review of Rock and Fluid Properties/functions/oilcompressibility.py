def oilcompressibility(pressure2, P_bubble, temp2, api, Rsb, sg2):
  import numpy as np
  from math import e

  # oil isothermal compressibility

  coil_array = []

  for i in range(len(pressure2)):
    if pressure2[i] < P_bubble:
      # use McCain
      ln_coil = -7.573 - (1.45 * np.log(pressure2[i])) - (0.383 * np.log(P_bubble)) + (1.402 * np.log(temp2)) + (0.256 * np.log(api)) + (0.449 * np.log(Rsb))  
      coil = np.exp(ln_coil)
    if pressure2[i] >= P_bubble:
      # use Vazquez-Beggs
      coil = ((5 * Rsb) + (17.2 * temp2) - (1180 * sg2) + (12.61 * api) - 1433) / (1E+05 * pressure2[i])
    coil_array.append(float(coil))
  return(coil)