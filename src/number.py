'''
Created on May 3, 2012

@author: valeriy
'''

class Number:
    def __init__( self, value ):
        self.value = value
        self.divisors = self._getDivisors()
        self.subsets = self._getDivisorSubsets()

    def _getDivisors( self ):
        "Get a list of all divisors of <self.value> - excluding <self.value> itself"
        divisors = [1]
        for num in range( 2, ( self.value / 2 + 1 ) ):
            if ( self.value % num ) == 0:
                if num in divisors:
                    break
                i = self.value / num
                if i == num:
                    divisors.append( num )
                else:
                    divisors.extend( [num, self.value / num] )

        return divisors

    def _getDivisorSubsets( self ):
        "Get a list containing all subsets of <self.divisors>"
        f = lambda l: reduce( lambda z, x: z + [y + [x] for y in z], l, [[]] )
        subsets = f( self.divisors )
        return subsets

    def isOfInterest( self ):
        """Check if given <self.value> satisfies following requirements:
            1. sum(self.divisors) > self.value
            2. No subset from <self.subsets> adds up to exactly <self.value>
        """
        isOfInterest = True

        if sum( self.divisors ) > self.value:
            for subset in self.subsets:
                if sum( subset ) == self.value:
                    isOfInterest = False
                    break
        else:
            isOfInterest = False

        return isOfInterest

