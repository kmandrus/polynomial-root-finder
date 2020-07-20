#import math

#Lists represent polynoimals in standard form. The value at index 0 represents the constant, or x^0, term,
#the value at index 1 is the coefficient of the x^1 term, and so on. 
#For example, [3, -2, -7, 15] represents 15x^3 - 7x^2 - 2x + 3.
#Roots are returned as a list as well. If a root has a multiplicity greater than one, it will show up a
#number of times equal to its multiplicity in the array.

#Currently, the primary function is findIntegerRoots. Everything else is a helper function or a test.
#Hopefully, rational and irrational roots will be implemented at some point.

#Find the quotient and remainder of a polynomial and a binomial.
#Parameters: Dividend (a polynomial) and divisor (a binomial with a leading coefficient of 1)
#Returns the quotient. (It does NOT return a remainder, if one exists. Use the faster, hasRemainder()
#function to check if a quotient has a remainder.) 
#Perhaps add functiionality for polynomials with a leading coefficient > 1?
def syntheticDivision(dividend, divisor):
	#ensure dividend's degree >= 2 and divisor is a binomial with a leading coefficient of 1?
	
	synDivisor = -divisor[0]
	column = len(dividend) - 1
	quotient = [dividend[pos]]
	workingValue = dividend[column] #Think of workingValue as the last value you wrote when doing the algorithm by hand.
	column -= 1
	while column >= 0:
		workingValue = workingValue * synDivisor + dividend[column]
		quotient.insert(0, workingValue)	
		column -= 1
	quotient.pop(0) #removes the remainder from the quotient. Could be returned if needed...
	return quotient

#Only works for the synthetic division setup of a polynomial divided by a binomial. 
def hasRemainder(dividend, divisor):
	#ensure divisor is a binomial with a leading coefficient of 1

	synDivisor = -divisor[0]
	sum = 0
	for i in range(len(dividend)):
		term = dividend[i]
		sum += term * synDivisor ** i

	if sum == 0:
		return False
	return True

#Finds all the divisors, positive and negative, of the int parameter "num." Returns an unsorted list.
def findDivisors(num):
	divisors = [num, -num]
	for d in range(1, (abs(num) // 2) + 1):
		if num % d == 0:
			divisors.append(d)
			divisors.append(-d)
	return divisors

#This function finds the integer roots of a polynomial with integer coefficients. 
#It takes a polynomial and returns its roots (in an array).
#If a root has a multiplicity of 3, that root will be present in the array 3 times.
def findIntegerRoots(poly):
	roots = []
	depressedPoly = poly.copy()
	#ensure the argument has integer coefficients.

	#factor out any powers of x common to all terms. Note that zero must be a root if we factored.
	#This boils down to checking for leading zeros in the list that represents the polynomial.
	#adds any zeros discovered by factoring to the list of roots
	#This breaks if passed a polynomial with all zero coefficients
	numZeros = 0
	for term in poly:
		if term == 0:
			numZeros += 1
			roots.append(0)
		else:
			break
	depressedPoly = depressedPoly[numZeros:]

	#All integer roots must divide the constant term of the factored polynomial.
	#Assemble the list of possible roots from the constant term.
	possibleRoots = findDivisors(depressedPoly[0])

	#pare down the list of roots using even/oddness and other commonsense tricks. (Unimplemented.)

	#Use hasRemainder() to check if the division has a remainder, then, if hasRemainder() returns false, 
	#syntheticDivision() to compute the division and depress the polynomial.
	for r in possibleRoots: 
		if len(depressedPoly) < 2:
			break
		divisor = [-r, 1]
		#implementing this as a while loop allows an easy check for multiplicity.
		while hasRemainder(depressedPoly, divisor) == False:
			roots.append(r)
			depressedPoly = syntheticDivision(depressedPoly ,[-r, 1])
			
	#Sort the list of roots?

	return roots

#Test Data

#prints a quotient tuple returned from the syntheticDivision function.
def printQuotient(q):
	print("(", q[0], ",", q[1], ")")

#Tests for Integer Roots
def testIntegerRoots():
	print(findIntegerRoots([-140, -204, -59, 6, 1])) #yields roots at -10, -2, -1, and 7
	print(findIntegerRoots([0, 0, 0, -2295, -3639, -1546, -202, 1, 1])) #yields roots at 0, -1, -3, -5, -9, 17
	print(findIntegerRoots([-1512, -1188, 270, 305, -15, -21, 1])) # -2, -2, -2, 3, 3, 21
	print(findIntegerRoots([5, 1])) # -5
testIntegerRoots()

#Tests for syntheticDivision()
def testSynthDiv():
	t1 = syntheticDivision([11, -1, 7, 1],[-5, 1]) #returns (306, [59, 12, 1])
	printQuotient(t1)
	t2 = syntheticDivision([-24, 17, 2, -9, 3], [-2, 1]) #returns (-6, [9, -4, -3, 3])
	printQuotient(t2)
	t3 = syntheticDivision([-6, -5, 2, 1], [-2, 1]) # returns (0, [3, 4, 1])
	printQuotient(t3)
#testSynthDiv()

#Tests for findDivisors()
def testFindDivisors():
	print(findDivisors(12))
	print(findDivisors(0))
	print(findDivisors(17))
	print(findDivisors(-1))
	print(findDivisors(-23))
	print(findDivisors(-24))
#testFindDivisors()

#tests for hasRemainder()
def testHasRemainder():
	print(hasRemainder([-10, -3, 1], [-5, 1])) #false
	print(hasRemainder([-10, -3, 1], [7, 1])) #true
	print(hasRemainder([4096, -2048, 384, -32, 1], [-8, 1]))
	print(hasRemainder([4096, -2048, 384, -32, 1], [-4, 1]))
#testHasRemainder()


