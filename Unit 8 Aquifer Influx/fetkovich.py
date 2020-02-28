def influx_matbalance_undersaturated(pressure, Bw, Wp, Np, Bo, Nfoi, cf, cw, swi, Boi, delta_time):
  "Eq 8.3"
  # in case of undersaturated (above bubblepoint), Rp = Rs = Rsi, Gfgi = Bgi = Eg = 0
  # pressure and Bo are pressure and oil FVF data over time (so, it must be in ARRAY)
  # Bw: water FVF (RB/STB)
  # Wp: cumulative water production (STB), in ARRAY
  # Np: cumulative oil production (STB), in ARRAY
  # Bo: oil FVF
  # Nfoi, Gfgi: original oil, gas, in place (cubic ft), from volumetrics
  # cf, cw: rock, water compressibility (psi^-1)
  # swi: initial water saturation
  # Boi, Bgi: initial oil, gas FVF 
  
  import numpy as np

  F = Np * Bo
  Eo = Bo - Boi
  delta_time = delta_time
  delta_pressure = pressure - pressure[0]
  delta_pressure = np.abs(delta_pressure)

  # Efw = ((4E-06 + (3E-06 * 0.48)) / (1 - 0.48)) * delta_pressure
  Efw = ((cf + (cw * swi)) / (1 - swi)) * delta_pressure

  We = (Bw * Wp) + F - (Nfoi * Eo) - ((Nfoi * Boi) * Efw)

  delta_We = [j-i for i, j in zip(We[:-1], We[1:])]
  delta_We = np.append([0], delta_We)
  We_rate = delta_We / delta_time

  return(delta_pressure, Efw, Eo, F, We, We_rate)

def influx_rate_schiltuis_general(F_rate, Bw, Wp_rate):
  "Eq 8.4"
  # F_rate: reservoir voidage rate
  # Bw: water FVF
  # Wp_rate: water production rate
  
  We_rate = F_rate + (Bw * Wp_rate)
  return(We_rate)

def influx_rate_schiltuis_nonvolatile(Bw, Wp_rate, Bo, Rs, Bg, Np_rate, Gp_rate):
  "Eq 8.5"
  # Bo, Bg: oil, gas FVF
  # Rs: solution gas-oil ratio (scf/STB)
  # Np_rate, Gp_rate: oil, gas production rate
  We_rate = (Bw * Wp_rate) + ((Bo - (Rs * Bg)) * Np_rate) + (Bg * Gp_rate)
  return(We_rate)

def influx_rate_schiltuis_undersaturated(Bw, Wp_rate, Bo, Np_rate):
  "Eq 8.6"
  # above bubblepoint pressure, P_bubble
  We_rate = (Bo * Np_rate) + (Bw * Wp_rate)
  return(We_rate)
