'''
Created on May 3, 2012

@author: valeriy
'''

def _powerset( seq ):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len( seq ) <= 1:
        yield seq
        yield []
    else:
        for item in _powerset( seq[1:] ):
            yield [seq[0]] + item
            yield item

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

    def powerset( self ):
        """
        Returns all the subsets of this set. This is a generator.
        """
        return _powerset( self.divisors )
