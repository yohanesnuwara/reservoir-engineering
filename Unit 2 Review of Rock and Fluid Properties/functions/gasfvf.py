def gasfvf(z, temp, pressure):
  Bg = 0.0282793 * z * temp / pressure # Eq 2.2, temp in Rankine, p in psia
  return(Bg
