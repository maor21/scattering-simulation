import matplotlib.pyplot as plt
import scatterer
import time
import math

def plot_intensity(sca, scatterer, time, location, wave):
    """ plots the intensity of the total field in a desired location
    from scatterer the function uses the field at the location
    """
        
# this function needs to be changed! I need to write the values of field for each scatterer in each time itteration. than I need to sum the fields from all scatterers in each time step.


    # h_fig = plt.figure()
    # h_ax  = plt.axes()
    # field = []
    # t     = list(range(time))

    # for i in range(len(sca)):
    #     field.append = sca['sca ' + str(i + 1)].measured_field(location, time, wave)

    # plt.plot(t, field)