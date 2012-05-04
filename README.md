pitchup
=======

REQUIREMENT:

Write a program to find a pitch based on this clue: 

"Join us at pitch x. x is a number between 1 and 553 such that the sum of x's divisors 
(not including x) is greater than x but no subset of x's divisors add up to exactly x."*

IMPLEMENTATION NOTES:

1. All "heavy lifting" is done within Number class (number.py). This class defines one public 
	method (getDivisorSubsets()) that returns a list of all possible subsets of given number's 
	divisors
	
2. Main program (pitchup.py) uses "threading" to validate each number in the range 1 ... 553 
	in parallel (multi-threading). This is very primitive use of "threading" - as there is no
	shared resources that would require use of Lock or RLock. Each thread executes checkNum()
	procedure which validates if given number passes our two main requirements. It first checks
	if the sum of all number's divisors (excluding the number itself) is greater that than the
	number itself, and if yes (this means given number passed first requirement) - we execute 
	num.getDivisorSubsets() to get complete list if divisor's subsets and check second 
	requirement. Checking sum(num.divisors) before getting the subsets list - eliminates 
	(potentially) the need to execute num.getDivisorSubsets() for some number which improves 
	overall performance (as num.getDivisorSubsets() - is takes lots of system resources) 
	
IMPORTANT:
	
Number.getDivisionSubsets() method (to be exact - inline procedure f() defined in that method) - 
can get extremely slow and can require lots of resources (CPU and memory) for some numbers. This
is explained by the number of permutations evaluated by this procedure when constructing a list of
all subsets of number's divisors set. I admit that given algorithm is far from optimal... I could 
probably come up with a better (but more complex) implementation of this algorithm - if I had taken 
more time to do so.


RESULT:

Given program (pitchup.py) finds only one solution to the given problem: 70

If I restrict this program to getting AT MOST one solution - it finds 70 quite quickly. But I
decided NOT to limit to just one result (to make sure there are no more possible results).

  