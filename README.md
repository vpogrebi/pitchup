pitchup
=======

REQUIREMENT:

Write a program to find a pitch based on this clue: 

"Join us at pitch x. x is a number between 1 and 553 such that the sum of x's divisors 
(not including x) is greater than x but no subset of x's divisors add up to exactly x."*

IMPLEMENTATION NOTES:

This project is implemeted using Python 2.7

1. All "heavy lifting" is done within Number class (number.py). This class defines one public 
	method (getDivisorSubsets()) that returns a list of all possible subsets of given number's 
	divisors. Number.getDivisorSubsets() uses lots of system resources (CPU and memory)
	and takes long time to execute for some numbers (the larger divisors set - the larger
	number of permutations are being evaluated) 
	
2. Main program (pitchup_threading.py) uses "threading" to validate each number in the 
	range 1 ... 553 in parallel (multi-threading). This is very primitive use of "threading" - 
	as there is no shared resources that would require use of Lock or RLock. Each thread 
	executes checkNum() procedure which validates if given number passes our two main 
	requirements. IMPORTANT: pitchup_threading.py - uses lots of system resources (CPU and memory)
	and takes long time to execute (see comments for Number.getDivisorSubsets() above)
	
3. To avoid users waiting for a long time for pitchup_threading.py to complete, I implemented
	second program - that searches for one single "pitch" and exits. "pitchup_single.py"
	finds expected result (70) quite quickly	

4. Both "pitchup_threading.py" and "pitchup_single.py" - implement checkNum() procedure that
	validates the number. It first checks if the sum of all number's divisors (excluding the 
	number itself) is greater that than the number, and if yes (this means given number passed 
	first requirement) - it executes num.getDivisorSubsets() to get complete list if divisor's 
	subsets and checks second requirement. Checking sum(num.divisors) before getting the subsets 
	list - eliminates (potentially) the need to execute num.getDivisorSubsets() for some numbers, 
	which improves overall performance (as num.getDivisorSubsets() - takes lots of system resources)
	
	
IMPORTANT:
	
Number.getDivisionSubsets() method (to be exact - inline procedure f() defined in that method) - 
can get extremely slow and can require lots of resources (CPU and memory) for some numbers. This
is explained by the number of permutations evaluated by this procedure when constructing a list of
all subsets of number's divisors set. The larger the number's divisors set (num.divisors) - the
larger number of permutations are being evaluated, and the more resources it takes to construct
the subsets list. I admit that given algorithm is far from optimal... I could probably come up 
with a better (but more complex) implementation of this algorithm - if I had taken more time to do so.


RESULT:

Given program (pitchup_single.py) finds following solution to the given problem: 70
