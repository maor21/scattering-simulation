class Wave:
    """This is an incident wave that exist within Medium, and interacts with Scatterers.
    Wave has speed (and/or wavelength)
    """

    def __init__(self, wave_speed = 20, wavelength = 20 ):
        self.wave_speed = wave_speed                            # the speed of the wave in m/s
        self.wavelength = wavelength                            # the wave's length between two peaks
        self.location   = 0                                     # the wave's location at t=0 in Medium


    def propogation(self):
        self.location = self.location + self.wave_speed         # self.wave_speed is multiply by 1 sec each itteration.
    