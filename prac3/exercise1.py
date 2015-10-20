#last time we did a very simplistic velocity analysis. 
#this time we want to do a few more locations

import toolbox
import numpy as np
import pylab

#--------------------------------------------------
#       useful functions
#-------------------------------------------------

None

if __name__ == "__main__":
        #initialise dataset
        print "initialising dataset"

        
        #apply TAR
        print "applying true amplitude recovery"
        
        #lets see how many cdps there are
        print  np.unique(workspace['cdp'])[25::45].tolist()
        
        #copy your list of cdps here... it will make it easier later
        cdps = None
        
        params['velocities'] = None
        params['smoother'] = 1
        for cdp in cdps:
                pass
                
        vels = {}

        
        #build our 2D  velocity map
        print "building velocities"
        
        #view it
        pylab.imshow(params['vels'].T, aspect='auto')
        pylab.colorbar()
        pylab.show()
        
        #Now we have a better velocity profile, we can use a better nmo to move it out
        print "applying nmo correction"

        
        #apply AGC
        print "applying AGC"

        
        #trace mix
        print "applying trace mix"

        
        #stack
        print "stacking"

        #save a copy
        print "saving"
        
        #display
        #turn off gather sort
        params['primary'] = None
        print "displaying"

        
        
        
        














        