def trapezoid(y_vals, h):
  import numpy as np
  # simplification: V = h/2*(a1+an) + h/2(2*a2+2*a3+2*an-1) as V = first_term + second_term
  first_term = 0.5 * h * (y_vals[0] + y_vals[-1])

  # delete a0 and an
  y_trapez = np.delete(y_vals, 0)
  y_trapez = np.delete(y_trapez, -1)

  second_term = np.sum(2 * y_trapez)
  second_term = 0.5 * h * second_term
  return first_term + second_term
