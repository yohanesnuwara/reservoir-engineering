def calculate_parameter_VEH(index, t_DR_factor):
  "Van Everdingen-Hurst Unsteady State Method to calculate aquifer influx"
  import numpy as np
  t_DR_arr = []
  W_eD_arr = []

  for i in range(len(delta_time[index])):
    t_DR = t_DR_factor * (delta_time[index])[i]

    "calculate W_eD using Eq 6.36 and 6.37 for infinite reservoir (See: 6_examples_part2.ipynb)"
    if t_DR > 0.01 and t_DR <= 200:
      # use Eq 6.36
      W_eD = ((1.12838 * np.sqrt(t_DR)) + (1.19328 * t_DR) + (0.269872 * t_DR * np.sqrt(t_DR)) + (0.00855294 * (t_DR**2))) / (1 + (0.616599 * np.sqrt(t_DR) + (0.0413008 * t_DR)))
    if t_DR > 200:
      # use Eq 6.37
      W_eD = ((2.02566 * t_DR) - 4.29881) / np.log(t_DR)
      
    W_eD_arr.append(float(W_eD))
    t_DR_arr.append(float(t_DR))
    
  return(t_DR_arr, W_eD_arr)
