Polynomial Root Finder

Find integer, rational, and irrational roots of polynomials. 

This project was inspired by how awful it is to implement these algorithms by hand. I wanted a simple tool I could use to check my work as a math teacher.

Currently, this project only finds the integer roots of polynomials with integer coefficients. Call the findIntegerRoots() function and pass it a list that represents a polynomial. The zero index is the constant, and each successive position contains the coefficient for the corrosponding power of x. For example:

	[9, 3, 1] = x^2 + 3x + 9

The function will return the list of roots. If the multiplicity of a root is greater than one, the root will show up that many times in the list.