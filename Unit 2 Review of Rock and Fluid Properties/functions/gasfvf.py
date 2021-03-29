def gasfvf(unit='cuft/scf', z, temp, pressure):
  """
  Gas FVF calculated in user specified unit
  input: unit of choice (cuft/scf, rb/scf, rm3/stdm3), zfactor, temperature (deg Farenheit) and pressure (psia).
  """
  temp=temp+460
  if unit == 'cuft/scf':
    return (0.0282793 * z * temp / pressure)
  elif unit == 'rb/scf':
    return(0.00503676 * z * temp / pressure) 
  elif unit == 'rm3/stdm3':
    return(0.350958 * z * temp / pressure)
  else:
    print ("Unit not recognized, kindly use the appropriate unit")
    return None
