"Code Written by Mark Burgoyne (Santos), with permission, @vinomarkus in GitHub"


# Algorithm based on SPE15433, M.A Klins, A.J. Bouchard, C.L. Cable, 1988
# Note: Not using the Tcross function to evakuate whether in infinite or finite acting as this can result in
# inconsistencies. Instead simply evauate both and chose the highest value for Pd or lowest value for Qd

from scipy.special import j1
from scipy.special import j0
import math
import mpmath

def csch(x):
    if x > 100:
        return 0
    else:
        return float(mpmath.csch(x))
def beta(b, rd):

    return b[0] + b[1] * csch(rd) + b[2] * rd ** b[3] + b[4] * rd ** b[5]

# Solution for constant Terminal Rate at aquifer inner boundary

def pd(rd, td):
    if td < 0.01:
        return 2 * td ** 0.5 / 3.14159265359
    else:
        pd_inf = ((107.5868 * (td ** 0.5003552)) + (37.60613 * td) + (7.038188 * (td ** 1.338479))) / (
                    95.13748 + (77.0034 * (td ** 0.5003552)) + (16.63856 * td) + (td ** 1.338479))

        # Appendix B
        b1 = [-0.00870415, -1.08984, 12.4458, -2.8446, 3.4234, -0.949162]
        b2 = [-0.0191642, -2.47644, 25.3343, -2.73054, 6.13184, -0.939529]
        beta1 = beta(b1, rd)
        beta2 = beta(b2, rd)
        J1Beta1 = j1(beta1)
        J1Beta2 = j1(beta2)
        J1Beta1rd = j1(beta1 * rd)
        J1Beta2rd = j1(beta2 * rd)

        pd_fin = (2 / ((rd ** 2) - 1)) * (td + 0.25) - (
                    (3 * (rd ** 4)) - (4 * (rd ** 4) * math.log(rd)) - (2 * (rd ** 2)) - 1) / (
                             4 * (((rd ** 2) - 1) ** 2)) + (2 * math.exp(-(beta1 ** 2) * td) * (J1Beta1rd ** 2) / (
                    (beta1 ** 2) * ((J1Beta1rd ** 2) - (J1Beta1 ** 2)))) + (
                             2 * math.exp(-(beta2 ** 2) * td) * (J1Beta2rd ** 2) / (
                                 (beta2 ** 2) * ((J1Beta2rd ** 2) - (J1Beta2 ** 2))))
    return max(pd_inf, pd_fin)


# Solution for constant Terminal Pressure at aquifer inner boundary
def qd(rd, td):
    if td < 0.01:
        return 2 * td ** 0.5 / 3.14159265359 ** 0.5
    else:
        b = [1.129552, 1.160436, 0.2642821, 0.01131791, 0.5900113, 0.04589742, 1.0, 0.5002034, 1.50, 1.979139]
        qd_inf = (b[0] * td ** b[7] + b[1] * td + b[2] * td ** b[8] + b[3] * td ** b[9]) / (
                    b[4] * td ** b[7] + b[5] * td + b[6])
        if rd > 100:
            return qd_inf

        b1 = [-0.00222107, -0.627638, 6.277915, -2.734405, 1.2708, -1.100417]
        b2 = [-0.00796608, -1.85408, 18.71169, -2.758326, 4.829162, -1.009021]

        alpha1 = beta(b1, rd)
        alpha2 = beta(b2, rd)
        J0Alpha1 = j0(alpha1)
        J0Alpha2 = j0(alpha2)
        J1Alpha1rd = j1(alpha1 * rd)
        J1Alpha2rd = j1(alpha2 * rd)

        qd_fin = (rd ** 2 - 1) / 2 - (2 * math.exp(-alpha1 ** 2 * td) * J1Alpha1rd ** 2) / (
                    alpha1 ** 2 * (J0Alpha1 ** 2 - J1Alpha1rd ** 2)) - (
                             2 * math.exp(-alpha2 ** 2 * td) * J1Alpha2rd ** 2) / (
                             alpha2 ** 2 * (J0Alpha2 ** 2 - J1Alpha2rd ** 2))
    return min(qd_inf, qd_fin)
