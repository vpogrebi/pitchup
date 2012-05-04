'''
Created on May 3, 2012

@author: valeriy
'''

import time
import threading
from number import Number

def checkNum( num ):
    "Check if given number <num> passes requirements"
    num = Number( num )
    if num.isOfInterest():
        print "Selected pitch: %i (Divisors: %s, Subsets: %s)" % ( num.value, num.divisors, num.subsets )

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
