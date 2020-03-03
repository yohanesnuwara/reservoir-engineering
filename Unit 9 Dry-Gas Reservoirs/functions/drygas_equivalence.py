def condensate_to_gas_equivalence(api, stb):
  "Derivation from real gas equation"
  Tsc = 519.57 # standard temp in Rankine
  psc = 14.7 # standard pressure in psi
  R = 10.732
  rho_w = 350.16 # water density in lbm/STB

  so = 141.5 / (api + 131.5) # so: specific gravity of oil (dimensionless)
  Mo = 5854 / (api - 8.811) # molecular weight of oil
  n = (rho_w * so) / Mo  

  V1stb = ((n * R * Tsc) / psc)
  V = V1stb * stb
  return(V)

def general_equivalence(gamma, M):
  "Calculate equivalence of 1 STB of water/condensate to scf of gas"
  # gamma: specific gravity of condensate/water. oil specific gravity use formula: so=141.5/(api+131.5). water specific gravity = 1
  # M: molecular weight of condensate/water. oil: Mo = 5854 / (api - 8.811). water: Mw = 18
  V1stb = 132849 * (gamma / M)
  return(V1stb)
