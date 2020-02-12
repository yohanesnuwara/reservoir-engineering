def pbubble_vazquez(Rsb, sg2, api, temp2):
  import numpy as np
  # c1, c2, c3 coefficient from Vazquez-Beggs
  if api <=30:
    c1 = 0.0362
    c2 = 1.0937
    c3 = 25.7240
  if api > 30:
    c1 = 0.0178
    c2 = 1.187
    c3 = 23.9310

  P_bubble_vaz = (Rsb / (c1 * sg2 * np.exp((c3 * api)/(temp2 + 459.67))))**(1 / c2) # convert temp to Rankine
  return(P_bubble_vaz)