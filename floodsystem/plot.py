import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np 
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
    """Plot water levels for a station over time."""
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    poly, d0 = polyfit(dates, levels, p)

    """Plot water levels and a polynomial fit for a station over time."""
    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial is evaluated using the shift x)
    x1 = np.linspace(d0, x[-1], 30)
    plt.plot(x1, poly(x1 - d0))
    
    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.show()