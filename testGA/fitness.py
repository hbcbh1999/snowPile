# Package importation
import numpy as np
import sys
from problemSetup import *

################################################################################
#                                    INPUTS                                    #
################################################################################
# Get the inputs from the terminal line
gen = int(sys.argv[1])

################################################################################
#                                   MAIN BODY                                  #
################################################################################
# Get the values of the search space
var = np.genfromtxt('./gen%i/pop' %(gen))

# Loop over all individuals
for ind in range(Nind):
	# Get the lift, drag and area values for each individual
    cDi = var[ind,0]**2
    Mr = (var[ind,0]-2)**2
    # Save the values of the search space and the function value toghether in a file
    with open('./data/gen%i.txt' %gen, 'a') as file:
        for i in range(Nvar):
            file.write("%.6f, " %(var[ind,i]))
        file.write("%.6f, " %(cDi))
        file.write("%.6f \n" %(Mr))