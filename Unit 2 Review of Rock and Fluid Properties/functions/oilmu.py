def oilmu(pressure2, P_bubble, sg2, api, temp2, Rsb):
  # Calculate viscosity of oil
  import numpy as np

  mu_oil_array = []

  for i in range(len(pressure2)):
    if pressure2[i] <= P_bubble:
      if api <=30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
      if api > 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310

      # use Beggs and Robinson
      # valid for: 0 < pressure < 5250 psig, 70 < temp < 295 F, 20 < Rs < 2070 scf/STB, 16 < api < 58 API 
      x = (temp2**(-1.163)) * np.exp(6.9824 - (0.04658 * api))
      mu_dead_oil = 10**x - 1
      Rs = (pressure2[i]**c2) * c1 * sg2 * np.exp((c3 * api) / (temp2 + 459.67)) # gas-oil ratio at any pressure BELOW BUBBLEPOINT using Vazquez-Beggs
      a = 10.715 * ((Rs + 100)**(-0.515))
      b = 5.44 * ((Rs + 150)**(-0.338))
      mu_live_oil = a * (mu_dead_oil**b)

    if pressure2[i] > P_bubble:
      if api <=30:
        c1 = 0.0362
        c2 = 1.0937
        c3 = 25.7240
      if api > 30:
        c1 = 0.0178
        c2 = 1.187
        c3 = 23.9310

      # use Vazquez and Beggs
      # valid for: 126 < pressure < 9500 psig, 9.3 < Rs < 2199 scf/STB, 15.3 < api < 59.5 API, 0.511 < sg < 1.351 

      # compute oil viscosity at bubblepoint first
      x_bubble = (temp2**(-1.163)) * np.exp(6.9824 - (0.04658 * api))
      mu_dead_oil_bubble = 10**x_bubble - 1
      Rsb = (P_bubble**c2) * c1 * sg2 * np.exp((c3 * api) / (temp2 + 459.67)) # gas-oil ratio at any pressure BELOW BUBBLEPOINT using Vazquez-Beggs
      a_bubble = 10.715 * ((Rsb + 100)**(-0.515))
      b_bubble = 5.44 * ((Rsb + 150)**(-0.338))
      mu_live_oil_bubble = a_bubble * (mu_dead_oil**b_bubble)

      m = 2.6 * (pressure2[i]**1.187) * np.exp(-11.513 - (8.98E-05 * pressure2[i]))
      mu_live_oil = mu_live_oil_bubble * ((pressure2[i] / P_bubble)**m)
    mu_oil_array.append(float(mu_live_oil))
  return(mu_oil_array)