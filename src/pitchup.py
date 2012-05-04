'''
Created on May 3, 2012

@author: valeriy
'''

import time
import threading
from number import Number

pitches = []

def powerset( seq ):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len( seq ) <= 1:
        yield seq
        yield []
    else:
        for item in powerset( seq[1:] ):
            yield [seq[0]] + item
            yield item

def checkNum( num ):
    """Check if given <num.value> satisfies following requirements:
        1. sum(num.divisors) > num.value
        2. No subset from powerset of <num.divisors> adds up to exactly <num.value>
    """
    global pitches

    num = Number( num )

    isOfInterest = True

    if sum( num.divisors ) > num.value:
        subsets = powerset( num.divisors )
        for subset in subsets:
            if sum( subset ) == num.value:
                isOfInterest = False
                break
    else:
        isOfInterest = False

    if isOfInterest:
        pitches.append( num.value )

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
    if pitches != []:
        for pitch in pitches:
            print "Selected pitch: %i" % pitch
    else:
        print "No pitch selected"
