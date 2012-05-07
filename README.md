pitchup
=======

REQUIREMENT:

Write a program to find a pitch based on this clue: 

"Join us at pitch x. x is a number between 1 and 553 such that the sum of x's divisors 
(not including x) is greater than x but no subset of x's divisors add up to exactly x."*


IMPLEMENTATION NOTES:

This project is implemented using Python 2.7

There have been few rafactoring iterations - that gradually improved program's performance, 
ultimately leading to the given, quite well performing implementation.

If interested in details (to see how each refactoring iteration led to performance improvements) -
contact developer at vpogrebi@iname.com. Notes below correspond to the latest (most current)
implementation:

1. Number class (number.py) is used as helper. It implements methods that load number's divisors
	set (__loadDivisors()) and a generator method powerset() that returns POWERSET of number's 
	divisors. 

2. Main program (pitchup.py) uses "threading" to evaluate all individual numbers (in the range
	1 .. 553) in parallel. This is very primitive use of threading - as this program does not
	involve resource sharing that would require use of locking (Lock or RLock), notifications, etc.

3. All "heavy lifting" is done within number._powerset() procedure - which implements GENERATOR
	design pattern. Instead of loading entire POWERSET (a set of all subsets) of number's divisors
	into memory (which proved to be highly resource-bound and time consuming process), this procedure
	allows getting POWERSET items iteratively, one at a time. This results in really *huge* 
	performance improvements - due to the fact that instead of generating entire POWERSET (as I had 
	in previous iterations) and evaluating individual subsets after that, we now evaluate each 
	individual subset as it gets fetched by generator, and stop processing as soon as we find one 
	subset that does not pass validation. This saves time, memory, and avoids generating 
	(potentially large number of) subsets that are not needed for our evaluation   

	
RESULT:

Program (pitchup.py) finds (quite quickly) following solution to the given problem: 70
