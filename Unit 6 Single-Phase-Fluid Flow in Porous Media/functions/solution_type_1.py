def solution_type_1(time, poro, ct, k, rw, h, mu_oil, pi, re, q, Bo):
  
  "Chap 6.3 Constant-Rate Solutions: Bounded Cylindrical Reservoir"
  
  import numpy as np
  
  # rw_conv = rw * 0.08333 # from in to ft 
  r_eD = re / rw_conv
  t_Dw = 0.25 * r_eD**2
  t_finite_acting = (poro * mu_oil * ct * (rw_conv**2) * t_Dw) / (0.0002637 * k) # result in hour

  t_status_array = [] # finite or infinite
  P_wellbore_array = []
  T_Dw_array = []
  P_D_array = []
  equation_array = []

  for i in range(len(time)):

    if time[i] == time[0]:

      # at initial time, time is in INFINITE ACTING condition
      t_status = "infinite"
      t_status_array.append(t_status)

      # because initial time < t_finite_acting, equation used is automatically Eq 6.20
      eq = "6.20"
      equation_array.append(eq)

      T_Dw = (0.000263 * k * time[i]) / (poro * mu_oil * ct * (rw_conv**2))
      T_Dw_array.append(float(T_Dw))

      P_D = "NaN"
      P_D_array.append(float(P_D))

      P_wellbore = pi
      P_wellbore_array.append(float(P_wellbore))

    if time[i] != time[0]:
      if time[i] < t_finite_acting:
        # time is in INFINITE ACTING CONDITION
        t_status = "infinite"
        t_status_array.append(t_status)

        # criteria to determine whether using Eq 6.20 (Lee simplification of Eq 6.17's using Bessel function) is valid

        eq = "6.20"
        equation_array.append(eq)

        T_Dw = (0.000263 * k * time[i]) / (poro * mu_oil * ct * (rw_conv**2))
        T_Dw_array.append(float(T_Dw))

        if T_Dw > 100:
          P_D = 0.5 * (((np.log(T_Dw)) + 0.80907)) # Eq 6.20
          P_D_array.append(float(P_D))

          # re-arranging Eq 6.15 to calculate P_wellbore
          P_wellbore = pi - ((P_D * q * Bo * mu_oil) / (0.007082 * k * h))
          P_wellbore_array.append(float(P_wellbore))

        if T_Dw < 100:
          P_D = "NaN"
          P_D_array.append(float(P_D))

          P_wellbore = "NaN"
          P_wellbore_array.append(float(P_wellbore))

      elif time[i] >= t_finite_acting:
        # time is in FINITE ACTING CONDITION
        t_status = "finite"
        t_status_array.append(t_status)

        # criteria to determine whether using Eq 6.19 (Lee simplification of Eq 6.17's using Bessel function) is valid

        eq = "6.19"
        equation_array.append(eq)

        T_Dw = (0.000263 * k * time[i]) / (poro * mu_oil * ct * (rw_conv**2))
        T_Dw_array.append(float(T_Dw))

        if T_Dw > 25:
          P_D = (2 * T_Dw / (r_eD**2)) + np.log(r_eD) - 0.75 # Eq 6.19
          P_D_array.append(float(P_D))
          
          # re-arranging Eq 6.15 to calculate P_wellbore
          P_wellbore = pi - ((P_D * q * Bo * mu_oil) / (0.007082 * k * h))
          
          P_wellbore_array.append(float(P_wellbore))

        if T_Dw < 25:
          P_D = "NaN"
          P_D_array.append(float(P_D))

          P_wellbore = "NaN"
          P_wellbore_array.append(float(P_wellbore))

  return(t_status_array, P_wellbore_array, T_Dw_array, P_D_array, equation_array, t_finite_acting) # T_Dw_array, P_D_array, equation_array are not necessary. P_wellbore is the result.
