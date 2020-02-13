def extrapolatepressure_gas(sg, pressure, temp, delta):
  import numpy as np
  R = 10.732

  rhogas = (28.97 * sg * pressure) / (z * R * (temp + 459)) # temp convert to Rankine

  # gas density gradient

  rhogas_grad = rhogas / 144

  # extrapolate using Eq 3.1

  pressure_extrapolated_below = pressure + rhogas_grad * delta
  pressure_extrapolated_above = pressure - rhogas_grad * delta
  
  # or extrapolate using Eq 3.7
  
  pressure_extrapolated_below2 = pressure*(np.exp((0.01877 * sg * delta) / (z * (temp + 459)))) # temp in Rankine
  pressure_extrapolated_above2 = pressure*(np.exp(-(0.01877 * sg * delta) / (z * (temp + 459)))) # temp in Rankine
  
  return(pressure_extrapolated_below, pressure_extrapolated_above, pressure_extrapolated_below2, pressure_extrapolated_above2)
