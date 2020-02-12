def gasoilratio(pressure2, P_bubble, sg2, api, temp2, Rsb):
  import numpy as np
  Rs_array = []

  for i in range(len(pressure2)):
    if pressure2[i] < P_bubble:
      if api <=30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
      if api > 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310

      Rsc = (pressure2[i]**c2) * c1 * sg2 * np.exp((c3 * api) / (temp2 + 459.67)) # gas-oil ratio at any pressure BELOW BUBBLEPOINT using Vazquez-Beggs
      Rs = Rsc
    if pressure2[i] >= P_bubble:
      Rs = Rsb
    Rs_array.append(float(Rs))
  return(Rs_array)
