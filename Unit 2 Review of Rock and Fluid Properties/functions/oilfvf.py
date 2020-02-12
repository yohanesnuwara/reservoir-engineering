def oilfvf(P_bubble, api, Rsb, sg2, temp2, pressure2):
  import numpy as np
  # FVF of oil at bubblepoint pressure using Levitan-Murtha
  so = 141.5 / (api + 131.5)
  Bo_bubble = 1 + ((0.0005 * Rsb) * ((sg2 / so)**0.25)) + ((0.0004*(temp2- 60)) / (so * sg2)) # temp in def F

  Bo_array = []

  for i in range(len(pressure2)):
    if pressure2[i] < P_bubble: # use Vazquez-Beggs
      if api <= 30:
        # use Vazquez-Beggs 
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
        c4 = 4.677E-4
        c5 = 1.751E-5
        c6 = -1.811E-8
      if api <= 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310
        c4 = 4.670E-4
        c5 = 1.100E-5
        c6 = 1.337E-9
      Rsc = (pressure2[i]**c2) * c1 * sg2 * np.exp((c3 * api) / (temp2 + 459.67))
      Bo = 1 + (c4 * Rsc) + (c5 * (temp2 - 60) * (api / sg2)) + (c6 * Rsc *(temp2 - 60) * (api / sg2)) # temp in deg F
    if pressure2[i] == P_bubble:
      # use Levitan-Murtha
      Bo = Bo_bubble
    if pressure2[i] > P_bubble:
      # use Levitan-Murtha
      coil = ((5 * Rsb) + (17.2 * temp2) - (1180 * sg2) + (12.61 * api) - 1433) / (1E+05 * pressure2[i])
      Bo = Bo_bubble * np.exp(coil * (P_bubble - pressure2[i]))
    Bo_array.append(float(Bo))
    return(Bo_array)
