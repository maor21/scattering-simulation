
class Medium:
    """The space in which scatteres and waves axist.
    Medium holds the grid that is measured in nm
    
    
    Parameters
    ----------
    length: number
        the lenght of the medium
    width: number
        the width of the medium
    """


    def __init__(self, length = 700, width = 1000):
        self.length = length
        self.width  = width
        self.scat   = {}


    def set_location(self, phase_choice, N):
        """ determines the locations of all N comprising scatterers.
        the user can choose between an amorphous-like (random) arrangment
        to two crystalline-like cubic arrangments.
        phase choice = 0, 1, 2 respectively.
        """

        if phase_choice == 0:
            location = Medium.set_amorphous_location(self, N)
        elif phase_choice == 1:
            location = Medium.set_simple_cubic_location(self, N)
        elif phase_choice == 2:
            location = Medium.set_centered_cubic_location(self, N)
        else:
            print('Please choose 0 for amorphous, 1 for simple cubic, and 2 for faced centered cubic')

        return location

    def set_amorphous_location(self, N):
        """positions a scatterer in an amorphous fashion by picking random values
        whithin a square. returns loc = [x_value, y_value]
        """
        import random
        x   = self.length / 4
        y   = self.width / 2
        d   = self.length / 10                                                   # determines the size of the area where scatterers can exist
        z   = lambda a: random.random() * random.randrange(a - d, a + d)         # creates pair of random values within an accepted area
        loc = []
        for i in range(N):
            loc.append = [z(x), z(y)]                                            # the location [x,y] of a given scatterer
        return loc

    def set_simple_cubic_location(self, N):
        """positions a scatterer in a SIMPLE CUBIC arrangment picking values
        whithin a square. returns loc = [x_value, y_value]
        """
        d   = self.length / 10 
        x   = self.length / 4 - d
        y   = self.width / 2 + d
        n   = 4                                                                  # number of scatterers in each column
        loc = []
        for i in range(1, N + 1):
            k = range(1, 2 * (N + 1), 2)
            if i <= n:
                loc.append([x + d/4, y - k[i] * d/4])
            elif i > n and i <= 2 * n:
                loc.append([x + 3 * d/4, y - (k[i] - 2 * n) * d/4])
            elif i > 2 * n and i <= 4 * n:
                loc.append([x + 7 * d/4, y - (k[i] - 6 * n) * d/4])
        return loc

    def set_centered_cubic_location(self, N):
        """positions a scatterer in a FACED-CENTERED CUBIC arrangment picking values
        whithin a square. returns loc = [x_value, y_value]
        This method shift every second column of scatterers which was created by
        set_simple_cubic_location(), by d/4 upwards
        """
        d   = self.l / 10 
        n   = 4
        loc = Medium.set_simple_cubic_location(N)
        l   = []
        k   = list(range(1, N, 2 * n))
        for i in list(range(len(k))):
            l = l + list(range(k[i], k[i] + n))
        for i in l:
            loc[i - 1][1] = loc[i - 1][1] + d/4
        return loc


    def plot_medium():
        import matplotlib.pyplot as plt
        h_medium = {}
        h_fig = plt.figure()
        h_ax  = plt.axes()
        # line  = plt.scatter([0,1,2,3,4,5,6,7,8,9], [0,1,4,9,16,25,36,49,64,81])
        plt.show()
        return 