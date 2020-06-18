def simple_linear_regression_traditional(x, y):
  "Traditional linear regression with B0 intercept, B1 slope"
  import numpy as np
  x = np.array(x); y = np.array(y); x_test = np.array(x_test)
  mean_x = np.mean(x)
  mean_y = np.mean(y)
  err_x = x - mean_x
  err_y = y - mean_y
  err_mult = err_x * err_y
  numerator = np.sum(err_mult)
  err_x_squared = err_x**2
  denominator = np.sum(err_x_squared)
  B1 = numerator / denominator
  B0 = mean_y - B1 * mean_x
  return(B0, B1)
  
def simple_linear_regression_advanced(x, y):
  "Covariance method linear regression with B0 intercept, B1 slope"
  import numpy as np
  import statistics as stat
  x = np.array(x); y = np.array(y); x_test = np.array(x_test)
  mean_x = np.mean(x)
  mean_y = np.mean(y)
  stdev_x = stat.stdev(x)
  stdev_y = stat.stdev(y)
  cov_x_y = (np.sum((x - mean_x) * (y - mean_y))) * (1 / (len(x) - 1))
  corr_x_y = cov_x_y / (stdev_x * stdev_y)
  B1 = corr_x_y * (stdev_y / stdev_x)
  B0 = mean_y - B1 * mean_x
  return(B0, B1)
