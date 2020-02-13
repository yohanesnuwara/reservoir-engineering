def rhooilgrad(so, sg, Rs, Bo):
  # standard conditions

  temp_sc = 60 # in fahrenheit
  pressure_sc = 14.73 # 1 atm = 14.73 psia
  z_sc = 1 # gas z factor at standard condition
  
  Rs_converted = 940 * (1/5.6148) # convert to scf oil/scf gas

  # oil FVF at surface/standard condition using Standing correlation (Equation 2.37 See Unit 2)

  F = Rs * ((sg / so)**0.5) + (1.25 * temp_sc) # Rs must be in scf/STB
  Bo = 0.972 + (0.000147*(F**1.1756))

  # oil density at surface/standard condition

  rhowater = 62.366 # 1 g/cm3 = 62.366 lbm/ft3
  rhooil_sc = so * rhowater

  # gas density at surface/standard condition (Eq 2.23, real-gas law)

  R = 10.732 # gas constant in (ft3*psi)/(lb-mol*R)
  rhogas_sc = (28.97 * sg * pressure_sc) / (z_sc * R * (temp_sc + 459)) # temp converted to Rankine

  # finally, oil density at reservoir condition

  rhooil = (rhooil_sc + (rhogas_sc * Rs_converted)) / Bo

  # oil density gradient

  rhooil_grad = rhooil / 144 # 144 is factor conversion from density lbm/ft3 to psi/ft
  rhooil_grad_converted = rhooil_grad * (6.89476 / 0.3048) # convert from psi/ft to kPa/m
  return(rhooil_grad, rhooil_grad_converted)
