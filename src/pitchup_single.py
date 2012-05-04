'''
Created on May 3, 2012

@author: valeriy
'''

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

    return isOfInterest

def pitchup():
    "Find all numbers in the range 1 .. 553 that pass requirements"
    pitch = None

    for num in range( 1, 553 ):
        if checkNum( num ):
            pitch = num
            break

    if pitch:
        print "Selected pitch: %i" % pitch
    else:
        print "No pitch selected"


if __name__ == '__main__':
    pitchup()
