import matplotlib.pyplot as plt

def plot_simulation(sca, wave, n):
    """ plots the scatterers and the secondary wavefronts they emit.   
    from sca the function uses the locations and the number of wave fronts n, and from wave, the wavelength.
    """

    h_fig = plt.figure()
    h_ax  = plt.axes()

    x     = []
    y     = []
    for i in range(sca):
        x.append = sca['sca ' + str(i + 1)].location[0]
        y.append = sca['sca ' + str(i + 1)].location[1]

    for i in range (n):
        size = ((i + 1) * wave.wavelength) **2
        plt.scatter(x, y, s = size, c = 'None', edgecolors = 'black', alpha = 0.3)
    plt.scatter(x, y, s = size / 2, c = 'black')
    plt.show()