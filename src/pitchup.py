'''
Created on May 3, 2012

@author: valeriy
'''

import time
import threading
from number import Number

def checkNum( num ):
    """Check if given <self.value> satisfies following requirements:
        1. sum(self.divisors) > self.value
        2. No subset from <self.subsets> adds up to exactly <self.value>
    """
    num = Number( num )

    isOfInterest = True

    if sum( num.divisors ) > num.value:
        subsets = num.getDivisorSubsets()
        for subset in subsets:
            if sum( subset ) == num.value:
                isOfInterest = False
                break
    else:
        isOfInterest = False

    if isOfInterest:
        print "Selected pitch: %i (Divisors: %s, Subsets: %s)" % ( num.value, num.divisors, subsets )

def pitchup():
    "Find all numbers in the range 1 .. 553 that pass requirements"

    # Start all the threads - one for each number in range 1 ... 553
    for num in range( 1, 553 ):
        thread = threading.Thread( target = checkNum, name = "checkNum_%i" % num, args = ( num, ) )
        thread.start()

    # Wait for all threads to terminate
    while threading.activeCount() > 1:
        time.sleep( 1 )

    return

if __name__ == '__main__':
    pitchup()
    print "Done"
