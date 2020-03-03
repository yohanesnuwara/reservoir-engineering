def recovery_factor_drygas_waterdrive(swi, Bgi, sgr, Bga):
  "recovery factor of dry gas reservoir with waterdrive"
  # gas FVF at abandonment pressure (RB/scf)
  # sgr: residual gas saturation
  rf = (((1 - swi) / Bgi) - (sgr / Bga)) / ((1 - swi) / Bgi)
  return(rf)

def recovery_factor_drygas_volumetric(Bgi, Bga):
  "recovery factor of dry gas reservoir with NO waterdrive"  
  # gas FVF at abandonment pressure (RB/scf)
  # sgr: residual gas saturation
  rf = 1 - (Bgi / Bga)
  return(rf)
