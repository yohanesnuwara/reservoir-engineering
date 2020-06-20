"Material Balance for Gas-Condensate Reservoirs"

def condensate_belowdew(Bg, Bo, Rs, Rv, p, cw, cf, sw, We, Bw, Wp, Wi, Np, Gp, Gi):
  "Condensate reservoir material balance below dewpoint"
  Rsi, Rvi = Rs[0], Rv[0]
  Bgi, pi = Bg[0], p[0]
  deltaP = p - pi

  Btg = ((Bg * (1 - (Rs * Rvi))) + (Bo * (Rvi - Rv))) / (1 - (Rv * Rs))
  Bto = ((Bo * (1 - (Rv * Rsi))) + (Bg * (Rsi - Rs))) / (1 - (Rv * Rs))
  Eg = Btg - Bgi
  Efw = ((cf + (cw * sw)) / (1 - sw)) * deltaP
  deltaW = We - (Bw * (Wp - Wi))
  F = (Np * ((Bo - (Rs * Bg)) / (1 - (Rv * Rs)))) + ((Gp - Gi) * ((Bg - (Rv * Bo)) / (1 - (Rv * Rs))))
  return(F)

def condensate_abovedew(Bg, Rv, p, cw, cf, sw, We, Bw, Wp, Wi, Np, Gp, Gi):
  "Condensate reservoir material balance above dewpoint"
  Rvi = Rv[0]
  Rs = 1 / Rvi # theoretical
  Bo = Bg * Rs # theoretical

  Bgi, pi = Bg[0], p[0]
  deltaP = p - pi

  Eg = Bg - Bgi
  Efw = ((cf + (cw * sw)) / (1 - sw)) * deltaP
  deltaW = We - (Bw * (Wp - Wi))
  F = Bg * (Gp - Gi)
  return(F)
