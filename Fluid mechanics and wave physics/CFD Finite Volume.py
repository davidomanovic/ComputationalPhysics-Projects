import matplotlib.pyplot as plt
import numpy as np

# -*- coding: utf-8 -*-
"""
Finite volume fluid simulation
Simulate compressible Euler fluids

Created on Wed Aug 21 09:24:04 2024

@author: David
"""
R = -1 # right
L = 1 # left
aX = 1 # x-axis
aY = 0 # y-axis

def conserved_variable(rho, vx, vy, V):
    """
    Calculate conserved variable from primitive

    Parameters
    ----------
    rho : cell density matrix
    vx : cell x-velocity
    vy : cell y-velocity
    V : cell volume

    Returns
    -------
    Mass and momentum

    """
    m = rho * V # mass
    px = rho * V * vx # cell momentum about x-axis 
    py = rho * V * vy # cell momentum about y-axis
    return m, px, py


