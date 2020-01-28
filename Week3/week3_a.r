# A) Write a Python and R program that has the following:
#
# 	- Variable declarations
# 	- Functions
# 	- If/Else statements
# 	- Control Loops

# Variable declaration
# Reference:
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Operators
# Left assignment
x <- 42 # can be used anywhere
print(x)

x = 42 # can only be used in the top level as a "statement"
print(x)

## Right assignment
99 -> y
print(y) 

# Function(s)
# Reference:
#
# 	* https://cran.r-project.org/doc/manuals/r-release/R-intro.html#Writing-your-own-functions
#
double <- function(n) {
	return(n * 2)
}
print(double(x))

# If / Else 
# Reference:
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Operators
#	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#if
#
isEven <- function(n) {
	if (n %% 2 == 0) {
		TRUE
	} else {
		FALSE
	}
}
print(sprintf("Is Even: %d %s", 2, toString(isEven(2))))
print(sprintf("Is Even: %d %s", 5, toString(isEven(5))))

## Control Loops

# Reference: 
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#Looping

# 1) repeat
# Repeat until a even number greater than 9 is found
# Reference:
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#repeat
n <- 0
repeat {
	n <- n + 1
	if(n > 9 && isEven(n)) {
		break
	}
}
paste("First even number greater than 9: ", n)

# 2) while
# loop while the number is less equal than 10 and greater to 0
# Reference:
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#while
n <- 10
while (n > 0 && n <= 10) {
	n <- n - 1
	print(n)
}

# 3) for 
# Loop over a list's elements
# Reference:
# 	* https://cran.r-project.org/doc/manuals/r-release/R-lang.html#for
elems <- c(1, 2, 3, 99, 187)
for (n in elems) {
	print(sprintf("Double of %d is %d", n, double(n)), quote = FALSE)
}