def pyramid(y_vals, h):
  import numpy as np
  # sort out a_0 and a_n, calculate the first term, 1/3*delta_z*(a_0+a_n)

  minus_a0 = np.delete(y_vals, 0)
  minus_a0_an = np.delete(minus_a0, -1)
  first_term = y_vals[0] + y_vals[-1]

  # multiply the the first part of second term from sorted list: second_term_1 = (delta_z/3) * (2a1+2a2+...+2an-1)

  second_term_1 = 2 * (np.sum(minus_a0_an))

  # process the second part of second term from sorted list: second_term_2 = (delta_z/3) * (sqrt(a1*a2)+sqrt(a2*a3)+...+sqrt(an-2*an-1))

  second_term_2 = [np.sqrt(j*i) for i, j in zip(y_vals[:-1], y_vals[1:])]
  second_term_2 = np.sum(second_term_2)

  # oip_pyramid = first_term + second_term_1 + second_term_2

  return (h / 3) * (first_term + second_term_1 + second_term_2)