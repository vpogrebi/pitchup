'''
Created on May 3, 2012

@author: valeriy
'''

class Number:
    def __init__( self, value ):
        self.value = value
        self.divisors = None
        self.__loadDivisors()

    def __loadDivisors( self ):
        "Get a list of all divisors of <self.value> - excluding <self.value> itself"
        self.divisors = [1]
        for num in range( 2, ( self.value / 2 + 1 ) ):
            if ( self.value % num ) == 0:
                if num in self.divisors:
                    break
                i = self.value / num
                if i == num:
                    self.divisors.append( num )
                else:
                    self.divisors.extend( [num, self.value / num] )

    def getDivisorSubsets( self ):
        "Get a list containing all subsets of <self.divisors>"
        f = lambda l: reduce( lambda z, x: z + [y + [x] for y in z], l, [[]] )
        subsets = f( self.divisors )
        return subsets
