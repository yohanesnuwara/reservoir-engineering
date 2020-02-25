def xy_plot_constant_rate(dataframe, index):
  "code to determine slope and intercept of MTR semilog and LTR normal plot, and finite acting time"
  "input is DATAFRAME"
  
  import numpy as np

  # time to reach finite-acting (LTR)
  t_finite_acting = dataframe.t[index]

  # MTR region to calculate for permeability
  df1 = dataframe.iloc[:index+1, :] # cut dataframe from index 0 to index of end of straight line
  if df1.t[0] == 0:
    dff1 = df1.drop(df1.index[0]) # drop the first row with time=0, because when log operation is underway, log(0) = indefinite
  else:
    dff1 = df1
  x1 = np.log(np.array(dff1.t))
  y1 = np.array(dff1.p)

  # LTR region to calculate for skin factor
  dff2 = dataframe.iloc[index:, :] # cut dataframe from index of start of straight line to the last index
  x2 = np.array(dff2.t)
  y2 = np.array(dff2.p)

  # title and labels for semilog plot of MTR and LTR
  title1 = "Semilog Plot of Borehole Flowing Pressure vs Time"
  title2 = "Normal Plot of Borehole Flowing Pressure vs Time"
  x1label = "Time (hours)"; x2label = x1label
  y1label = "Flowing Pressure (psia)"; y2label = y1label

  return(x1, y1, x2, y2, t_finite_acting)

def perm_welltest(m, mu_oil, h, q, Bo, qB):
  "Calculate permeability from well-test analysis"
  "Applicability: all well-test types EXCEPT MULTIRATE DRAWDOWN TEST, since k = (162.6 * Bo * mu_oil) / (slope * h); q is exceptional"
  # all inputs are in OILFIELD UNITS, result in MILIDARCIES
  # input q = 0 and Bo = 0 if both are UNKNOWN, but rate-Bo is known (usually data presented in rate-Bo)
  # input qB = 0 if both q and Bo are KNOWN
  # input h = 0 if h is unknown, then permeability-factor (kh) will be calculated
  # m: slope of plot
  # c: intercept of plot
  
  import numpy as np

  if h == 0:
    if q == 0 and Bo == 0:
      kh = - (162.6 * qB * mu_oil) / m # perm factor (in mD-ft)
      k = "None"
    if qB == 0:
      kh = - (162.6 * q * Bo * mu_oil) / m # perm factor (in mD-ft)
      k = "None"
  else:
    if q == 0 and Bo == 0:
      k = - (162.6 * qB * mu_oil) / (m * h) # perm (in mD)
      kh = "None"
    if qB == 0:
      k = - (162.6 * q * Bo * mu_oil) / (m * h) # perm (in mD)
      kh = "None"
  return(k, kh)
  
def reservoir_size(m_star, poro, h, ct, q, Bo, qB):
  "Calculate reservoir size from CONSTANT-RATE and FINITE-BUILDUP TESTS"
  # all inputs are in OILFIELD UNITS, result in ft
  # input q = 0 and Bo = 0 if both are UNKNOWN, but rate-Bo is known (usually data presented in rate-Bo)
  # input qB = 0 if both q and Bo are KNOWN
  # input h = 0 if h is unknown, then permeability-factor (kh) will be calculated
  # m_star: slope of plot, m*
  
  import numpy as np

  m_star = np.abs(m_star)
  if q == 0 and Bo == 0:
    re = np.sqrt((0.07447 * qB) / (poro * h * ct * m_star))
  if qB == 0:
    re = np.sqrt((0.07447 * q * Bo) / (poro * h * ct * m_star))
  return(re)

def reservoir_pv(m_star, ct, q, Bo, qB):
  "Calculate reservoir pore volume from CONSTANT-RATE and FINITE-BUILDUP TESTS"
  # all inputs are in OILFIELD UNITS, result in ft
  # input q = 0 and Bo = 0 if both are UNKNOWN, but rate-Bo is known (usually data presented in rate-Bo)
  # input qB = 0 if both q and Bo are KNOWN
  # input h = 0 if h is unknown, then permeability-factor (kh) will be calculated
  # m_star: slope of plot, m*

  m_star = np.abs(m_star)
  if q == 0 and Bo == 0:
    vp = (0.23395 * qB) / (ct * m_star)
  if qB == 0:
    vp = (0.23395 * q * Bo) / (ct * m_star)
  return(vp)
