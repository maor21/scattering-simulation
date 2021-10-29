    #function run simulation
    
def run_simulation(sca, m, w, time):
    """ run_simulation takes care of all actions need to be done during an itteration.
    it checks whether wave hit each scatterer. if so, "turn it on". it makes sure each turned on scaterer emits
    secondary wave, and if it did, updates the secondary wave. it also measures the scattered field of each scatterer
    """


    for i in range(len(sca)):
        sca['sca' + str(i + 1)].state = m.check_hit(sca=sca, wave=w) # I still need to write this function in Wave
        


    return w, sca, m