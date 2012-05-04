pitchup
=======

REQUIREMENT:

Write a program to find a pitch based on this clue: 

"Join us at pitch x. x is a number between 1 and 553 such that the sum of x's divisors 
(not including x) is greater than x but no subset of x's divisors add up to exactly x."*

IMPLEMENTATION NOTES:

1. All "heavy lifting" is done within Number class (number.py). This class defines one public 
	method (isOfInterest()) and two protected methods that produce results that are used by
	isOfInterest() to decide whether given Number is of our interest (if it passes above requirements)

2. Main program (pitchup.py) uses "threading" to validate each number in the range 1 ... 553 
	in parallel (multi-threading). This is very primitive use of "threading" - as there is no
	shared resources that would require use of Lock or RLock 	
	
IMPORTANT:
	
Number._getDivisionSubsets() method (to be exact - inline procedure f() defined in that method) - 
can get extremely slow and can require lots of resources (CPU and memory) for some numbers. This
is explained by the number of permutations evaluated by this procedure when constructing a list of
all subsets of number's divisors set. I admit that given algorithm is far from optimal... I could 
probably come up with a better (but more complex) implementation of this algorithm - if I had taken 
more time to do so.


RESULT:

Given program (pitchup.py) finds only one solution to the given problem: 70

If I restrict this program to getting AT MOST one solution - it finds 70 quite quickly. But I
decided NOT to limit to just one result (to make sure there are no more possible results).

  