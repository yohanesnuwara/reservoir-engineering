def waterfvf(temp, p):
  "Water FVF (Bw)"
  # temp in Fahrenheit
  # p pressure in psia
  Vwp = (-1.95301E-9 * p * temp) - (1.72834E-13 * (p**2) * temp) - (3.588922E-7 * p) - (2.25341E-10 * p**2)
  Vwt = (-1E-2) + (1.33391E-2 * temp) + (5.50654E-7 * temp**2)
  Bw = (1 + Vwt) * (1 + Vwp)
  return(Bw)
