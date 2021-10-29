
# class Scatterer:
#     """The point objects which scatters the incident wave once hit by.
#     scatterers then emit circular wave with not phase (comared with
#     the incudent wave), and with the same energy (i.e. same wavelength.)
    
    
#     :location:  their location within the object Medium
#     :radius:    the distance of the first wavefront forom the scatterer
#     """

#     def __init__(self, medium, wave):
#         self.radius   = wave.wavelength               # the initial distance is the incident wavelength
#         self.location = medium.set_location()         # scatterer location is set by the medium

#     def update_secondary_wave(self, medium):
#         # this function updates the progress of the emmited wave. it uses medium.time, medium.wevelength and scatterer's
#         # location to calculate scatterer's wavefronts.
#         return ???


class Scatterer:
    def __init__(self):
        self.delta_r  = 1           # the distance from its location to the measurment
        self.location = []          # a set of two values (x,y) for its location
        self.state    = 0           # the state of scatterer refers to whether its emiting radiation or not. i.e., if it was hit by an incident wave.


    def measure_field(self, location, time, wave):
        """ this function measures for each scatterer the field of emmited
        radiation in a desired location. 
        location - the location in which the intensity is measured
        time     - the time passed since the the state of the scatterer went on
        """

        import math

        self.delta_r = math.sqrt((self.location[0] - location[0]) **2 + (self.location[1] - location[1]) **2)
        phi          = (2 * math.pi / wave.wavelength) * (self.delta_r - time / wave.wave_speed)
        field        = math.exp(1j * phi)
        return field

    
    def update_secondary(self, wave):
        """this function updates the number of wavefronts so by the end of the simulation we can draw them all.
        """

        n = round(self.delta_r / wave.wavelength)       # number of wavefronts
        # here I need to plot a new circle using scatter(). the size of the scatter() is given by the parameter 's' as an argument: s=size.
        # size is equal to the area of the circle. same in matlab.
        return n                                        # maybe we can plot only once at the end, so we would like to know how many wavefront are.
    
    def emitting(self, medium, wave):
        """this function checks if the wave hit the scatterer. If so, the scatterer
        emits a secondery wave. at the moment isotropicaly, in the future will be expanded.
        """

        wave_hit = medium.check_hit(self, wave)
        if wave_hit == 1:
            self.update_secondary(self, wave)
