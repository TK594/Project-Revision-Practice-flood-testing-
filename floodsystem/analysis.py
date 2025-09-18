import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates

def polyfit(dates, levels, p):
    """Fit a polynomial of degree p to water level data"""
    # Create set of data points (x, y) for polynomial fitting
    x = matplotlib.dates.date2num(dates)
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    poly = np.poly1d(p_coeff)
    
    return poly, x[0]
