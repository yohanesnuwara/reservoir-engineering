"Material Balance for Gas-Condensate Reservoirs"

def calculate_condensate_params(Rvi, Bgi):
    """
    Calculate theoretically the undefined properties of gas-condensate (Bo, Rs)

    Input:
    Rvi: initial Rv, float
    Bgi: initial Bg, float

    Output:
    Rsi: initial Rs, float
    Boi: initial Bo, float
    """

    Rsi = 1 / Rvi
    Boi = Rsi * Bgi

    return(Rsi, Boi)

def condensate_belowdew(Rs, Rv, Rsi, Rvi, Bo, Bg, Np, Gp):
    """
    Calculate the parameters for material balance plot of gas-condensate reservoirs
    below dewpoint pressure

    Input:
    Rs: array
    Rv: array
    Rsi: initial Rs, float (NOTE: if data doesn't provide, calculate it with calculate_condensate_params function)
    Rvi: initial Rv, float (from data Rv)
    Bo: array
    Bg: array
    Np: array
    Gp: array

    Material balance plots:
    * Plot 10.1: F vs Eg

    Output:
    F: array
    Eg: array

    """
    Btg = ((Bg * (1 - (Rs * Rvi))) + (Bo * (Rvi - Rv))) / (1 - (Rv * Rs)) # in RB/STB
    Bto = ((Bo * (1 - (Rv * Rsi))) + (Bg * (Rsi - Rs))) / (1 - (Rv * Rs)) # in RB/scf

    Gi = 0
    F = (Np * ((Bo - (Rs * Bg)) / (1 - (Rv * Rs)))) + ((Gp - Gi) * ((Bg - (Rv * Bo)) / (1 - (Rv * Rs))))
    Eg = Btg - Bg[0]
    return(F, Eg)

def condensate_abovedew(Bg, Bgi, Gp, Gpi):
    """
    Calculate the parameters for material balance plot of gas-condensate reservoirs
    above dewpoint pressure

    Input:
    Bg: array
    Bgi: initial Bg, float
    Gp: array
    Gpi: initial Gp, float

    Material balance plots:
    * Plot 10.1: F vs Eg

    Output:
    F: array
    Eg: array

    """
    Eg = Bg - Bgi
    F = Bg * (Gp - Gpi)
    return(F, Eg)
