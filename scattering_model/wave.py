class Wave:
    """This is an incident wave that exist within Medium, and interacts with Scatterers.
    Wave has speed (and/or wavelength)
    """

    def __init__(self, wave_speed = 1e-2, wavelength = 1e-1 ):
        self.wave_speed = wave_speed                            # the speed of the wave in m/s
        self.wavelength = wavelength                            # the wave's length between two peaks
        self.position   = 0                                     # the wave's location at t=0 in Medium


    def update_wave(self, time):
        self.position = self.wave_speed  * time                 # self.wave_speed is multiply by 1 sec each itteration.


    def check_end_of_wave(self, m):
        """ checks whether the wave left Medium. as long as wave within Medium, the experiment continues
        """
        bolean = False
        if self.position == m.length:
            bolean = True
        return bolean