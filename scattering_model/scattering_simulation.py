# simulation

import wave as w
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import os
from medium import Medium as m
from scatterer import Scatterer as s
import run_simulation

def simulation(number_of_scatterers, phase, Medium, Scatterer, Wave):
    """calculating iteration by itteration the location ow the incident wave,
    wheter or not the wave hit each scatterer, and the propogation of secondary waves.
    """

    # #============== inputs ==============
    if number_of_scatterers in locals():
        return
    else:
        number_of_scatterers = 16

    if phase in locals():
        return
    else:
        phase = 0

    #============== objects ==============

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

    # creating an object of class Wave - the incident wave that initiates the scattering
    t = 0                                           # time count for the simulation



    #============== simulation ==============

    bol = wave.check_end_of_wave()

    while bol == False:
        wave, sca, medium = run_simulation(w=wave, s=sca, m=medium, time=t)
        t += 1
        wave.position = wave.update_wave(time=t)
        for i in range(len(sca)):
            sca['sca ' + str(i + 1)].n     = sca['sca ' + str(i + 1)].update_n()
            sca['sca ' + str(i + 1)].field = sca['sca ' + str(i + 1)].update_field()
            sca['sca ' + str(i + 1)].state = sca['sca ' + str(i + 1)].update_state()
            # sca['sca ' + str(i + 1)].update_sca(time=t)







    #============== graphics ==============
    import plot_simulation
    import plot_intensity
    plot_simulation(sca, wave, 15)                  # n = 15 was plugged in manually. needs to be automatically from the scatterer with the min value of x.
    plot_intensity(sca)





