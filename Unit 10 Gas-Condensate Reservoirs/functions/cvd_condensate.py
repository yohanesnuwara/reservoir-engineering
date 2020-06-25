def cvd_condensate(z, z2, temp, p, Gp, Np, Vo):
    """
    Calculate volatile oil-gas ratio of condensate from Constant-Volume Depletion (CVD) Study
    Walsh and Towler (1995)

    Inputs
    z: measured gas-phase compressibility factor (array)
    z2: measured two-phase compressibility factor (array)
    p: measured pressure (array)
    Gp: gas produced in the PVT cell, in Mscf
    Np: condensate produced in the PVT cell, in STB
    Vo: condensate volume in the PVT cell
    """

    z_j = z; Gp_j = Gp * 1E+3; Np_j = Np; z2_j = z2; Vo_j = Vo

    # calculate gas FVF (Bg)
    Bg = (0.00503676 * z_j * (temp + 460)) / p  # in RB/scf

    # initial gas FVF
    Bgi = Bg[0]

    # initial Gfg
    Gfgi = Gp_j[-1]  # in scf

    # initial Nfo
    Nfoi = Np_j[-1]

    # calculate initial Vtg (Vtg1)
    Vtg1 = Gfgi * Bgi  # in res bbl

    # initial values for Eq 10.14
    ntj_nt1 = 1
    delta_ngj_to_nt1 = 0

    # empty arrays for appending
    Rvj_arr = []
    delta_Gpj_arr = []
    delta_Npj_arr = []
    Gfgj_arr = []
    Nfgj_arr = []
    Gj_arr = []
    Nj_arr = []

    for i in range(len(p) - 1):

        # Eq 10.13
        Vtoj = Vo_j[i] * Vtg1

        # Eq 10.14
        ntj_nt1 = ntj_nt1 - delta_ngj_to_nt1

        # Eq 10.15
        Vtoj_Vtgj = ((Vtg1 * z2_j[i] * p[0]) / (z2_j[0] * p[i])) * (ntj_nt1)

        # Eq 10.16
        Vtgj = Vtoj_Vtgj - Vtoj

        # Eq 10.17
        delta_Vtgj = Vtoj_Vtgj - Vtg1

        # Eq 10.18
        ngj_nt1 = (Vtgj * z_j[0] * p[i]) / (z_j[i] * Vtg1 * p[0])

        # Eq 10.19
        delta_ngj_to_ngj = delta_Vtgj / Vtgj

        # Eq 10.20
        delta_ngj_to_nt1 = delta_ngj_to_ngj * ngj_nt1

        if i == 0:
            # Eq 10.21
            delta_Gpj = Gp_j[i] - 0

            # Eq 10.22
            delta_Npj = Np_j[i] - 0

            # Eq 10.23
            Gj = Gfgi - delta_Gpj

            # Eq 10.24
            Nj = Nfoi - delta_Gpj

            # Eq 10.25
            Gfgj = Gfgi

            # Eq 10.26
            Nfgj = Nfoi

        if i > 0:
            # Eq 10.21
            delta_Gpj = Gp_j[i] - Gp_j[i - 1]

            # Eq 10.22
            delta_Npj = Np_j[i] - Np_j[i - 1]

            # Eq 10.23
            Gj = Gj - delta_Gpj_arr[-1]

            # Eq 10.24
            Nj = Nj - delta_Npj_arr[-1]

            # Eq 10.25
            Gfgj = (Vtgj * delta_Gpj) / delta_Vtgj

            # Eq 10.26
            Nfgj = (Vtgj * delta_Npj) / delta_Vtgj

        delta_Gpj_arr.append(delta_Gpj)
        delta_Npj_arr.append(delta_Npj)
        Gj_arr.append(Gj)
        Nj_arr.append(Nj)
        Gfgj_arr.append(Gfgj)
        Nfgj_arr.append(Nfgj)

        # Eq 10.27
        Gfoj = Gj - Gfgj

        # Eq 10.28
        Nfoj = Nj - Nfgj

        # Eq 10.29
        Boj = Vtoj / Nfoj

        # Eq 10.30
        Bgj = Vtgj / Gfgj

        # Eq 10.31
        Rsj = Gfoj / Nfoj

        # Eq 10.32
        Rvj = (Nfgj / Gfgj) * 1E+06  # result in STB/scf
        Rvj_arr.append(Rvj)

    Rv = Rvj_arr
    return(Rv)
