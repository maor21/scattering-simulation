# gui for simulating scattering

# ============ imports ============
# import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import numpy as np
import os
from medium import Medium
from wave import Wave
from scatterer import Scatterer


# ============ gui background ============
root   = Tk()
root.title('Scattering Simulation: Crystals Vs. Glass')
canvas = Canvas(root, height = 700, width = 1000, bg = 'grey')
canvas.pack()
main_frame = Frame(root, bg = 'white')
main_frame.pack()
main_frame.place(relheight = 0.6,relwidth = 0.8, relx = 0.01, rely = 0.08)


# ============ buttons ============
def choose_number_of_scatterers():
    N     = simpledialog.askinteger('Number of Scatterers', 'How many scatterers to create?')
    phase = simpledialog.askinteger('Choose Phase', 'For amorphous type 0; for simple cubic type 1; for centered cubic type 2')
    locs  = Medium.set_location(phase, N)
    canvas.create_polygon(locs)
    print(locs)
    # main_fig  = plt.Figure()
    # plot_main = Frame(main_frame)
    # l   = plt.plot(range(N), range(N))
    # plt.show()

def simulation():
    
    return

play_simulation      = Button(root, text = 'play_simulation', command = simulation)
play_simulation.pack()
number_of_scatterers = Button(root, text = 'Choose formation', command = choose_number_of_scatterers)
number_of_scatterers.pack()



root.mainloop()