import math

#This array represents a polynomial in standard form. Each index contains a coeffecient of the polynomial.
#The 0 index is the constant term, the 1 index is x^1, and so on.

polynomial = []

#This function finds the integer roots of a polynomial with integer coefficients. 
#It takes a polynomial (an array) and returns its roots (in an array).
#If a root has a multiplicity of 3, that root will be present in the array 3 times.
def findIntegerRoots(poly):
	roots = []
	#ensure the argument has integer coefficients.

	#factor out any powers of x common to all terms. Note that zero must be a root if we factored.

	#All integer roots must divide the constant term of the factored polynomial.
	#Assemble the list of possible roots, k, from the constant term.

	#pare down the list of roots using even/oddness and other commonsense tricks.

	#use polynomial division to check each possible root.
	#depress the polynomial each time
	#watch out for double roots!
	#Perhaps use some sophistication in selecting which root to check?

	#Sort the list of roots.
	return roots

#Find the quotient and remainder of a polynomial and a binomial.
#Takes a polynomial and a binomial as parameters (represented as in the findIntegerRoots function above).
#Returns a tuple. The first position contains a bool that indicates whether there is a remainder, and the second position contains the quotient. (It does NOT return a remainder.)
def syntheticDivision(dividend, divisor):
	i = 1
	synDivisor = -divisor[0]
	quotient = [dividend[0]]
	workingValue = dividend[0]
	hasRemainder = true
	while i < len(dividend) :
		workingValue = workingValue * synDivisor + divisor[i]
		quotient.append(workingValue)
		i += 1
	if quotient[-1] == 0:
		hasRemainder = false
	#oh god I have a problem with reversing the list!
	return (hasRemainder, quotient)

#Test Data
#[420, -228, -207, 12, 3] yields roots at -10, -2, -1, and 7
#[0, 0, 0, -2295, -3639, -1546, -202, 1, 1] yields roots at 0, -1, -3, -5, -9