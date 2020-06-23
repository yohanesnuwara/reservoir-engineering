def gasfvf(z, temp, pressure):
  """
  Gas FVF calculated in oilfield unit, result in RB/scf
  inputs temp in Rankine (Fahrenheit + 460), pressure in psia or psig
  """
  Bg = 0.0282793 * z * temp / pressure 
  return(Bg)

def gasfvf(unit='unit1', temp=186, pressure=2000):
  """
  Gas FVF calculated in other units
  unit: choice of units (unit1: RB/scf, unit2: res m3/std m3)
  for unit1, inputs temp in Rankine (Fahrenheit + 460), pressure in psia or psig
  for unit2, inputs temp in Kelvin, pressure in psia or psig
  """
  if unit == 'unit1':
    Bg = 0.00503676 * z * temp / pressure 
  if unit == 'unit2':
    Bg = 0.350958 * z * temp / pressure
  return(Bg)
