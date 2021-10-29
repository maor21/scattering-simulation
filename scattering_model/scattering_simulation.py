# simulation

# from tkinter import *
# from tkinter import simpledialog
# from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import os
from medium import Medium
from wave import Wave
from scatterer import Scatterer
from time import Time

def simulation(number_of_scatterers, phase, Medium, Scatterer, Wave, Time):
    """calculating iteration by itteration the location ow the incident wave,
    wheter or not the wave hit each scatterer, and the propogation of secondary waves.
    """

    if number_of_scatterers in locals():
        return
    else:
        number_of_scatterers = 16

    if phase in locals():
        return
    else:
        phase = 0

    
    # creating an object of class Medium where scattering occures
    medium = Medium()
        # creating a set of locations for each scatterers
    locs = medium.set_location(number_of_scatterers, phase)
    print(locs)


    # creating number_of_scatterers objects of class Scatterers
    sca = {}                                        # a dict listing all scatterers
    for i in range(number_of_scatterers):
        sca['sca ' + str(i + 1)] = Scatterer()
        sca['sca ' + str(i + 1)].location = locs[i]


    # creating an object of class Wave - the incident wave that initiates the scattering
    wave = Wave()

    # playing the simulation
    Time.t = Time.t + 1
    for i in range(number_of_scatterers):
        sca['sca' + str(i + 1)].play_secondery_wave # I still need to write this function in Wave




    # plotting the end picture
    import plot_simulation
    import plot_intensity
    plot_simulation(sca, wave, 15)                  # n = 15 was plugged in manually. needs to be automatically from the scatterer with the min value of x.
    plot_intensity(sca)





