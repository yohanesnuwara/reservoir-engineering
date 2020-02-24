"Calculate Skin Factor from Various Well-Test Techniques"

# b1hr: pressure value at 1 hour determined from regression equation of m and c

"constant rate"
t1hr = 1 # time at 1 hour
# m2 and c2 are slope and intercept of the second regression line from normal plot
b1hr = m2 * t1hr + c2 

# m (slope) is m from semilog MTR plot, m1_cycle 
s = 1.1513 * (((pi - b1hr) / np.abs(m1_cycle)) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

"multirate"
s = 1.1513 * ((c3 / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

"constant pressure"
b1hr = m * np.log10(1) + c4 # 1/q at 1 hour 
s = 1.1513 * ((b1hr / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

"constant rate buildup"
# tp: flow time
b1hr = c + m * np.log10(tp + 1)

s = 1.1513 * (((pwf - b1hr) / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

"multirate buildup"
b1hr = c + m * np.log10(tp + 1)

s = 1.1513 * (((pwf - b1hr) / m) - np.log10(k / (poro * mu_oil * ct * (rw**2))) + 3.2275)

"finite buildup"
# skin factor can't be determined
