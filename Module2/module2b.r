#
# Module 2b
# Author: Tristian Azuara
# Email: tristian.azuara@gmail.com
# UCLA: Introduction to Data Science
#

print('A). Concatenate a set of integers, and strings and assign to a data frame')
nums <- c(99, 88, 77, 44)
strs <- c('a', 'b', 'c', 'd')

myData <- data.frame(
	# combine them and produce a single column. There is a catch, 
	# the combined vector will hold strings (numbers were coerced into strings)
	values = append(nums, strs) 
)
print(myData)

print('B). Take that list from A). and than separate out the integers and strings')
split_types <- function(dataFrame) {
	# Empty / NULL collections
	a <- c() 
	b <- c()

	for (x in dataFrame$values) {
		# Attempt to cast, if it fails, place the value in the right collection
		if (!suppressWarnings(is.na(as.numeric(x)))) {
			a <- append(a, x)
		} else {
			b <- append(b, x)
		}
	}

	data.frame(nums=a, strs=b)
}
print(split_types(myData))

print('C) Create a function that computes the fibonacci sequence')
# https://en.wikipedia.org/wiki/Fibonacci_number
fibo <- function(n) {
	if (n == 0) { # base case 0
		return(0)
	}

	if (n == 1) { # base case 1
		return(1)
	}

	fibo(n - 1) + fibo(n - 2)
}
print(fibo(10)) # 55

print('D). Sort a list of unsorted integers in a dataframe')
unsorted <- data.frame(values=c(1, 3, 6, 22, 1, -2, 3, -33, -66, 77))
print(unsorted)

# The `order` function returns the indexes in the sorted order as a collection,
# we can then use that list to access the elements in the represented order.
ordered <- order(unsorted$values)
print(unsorted[ordered,]) # The trailing `,` indicates that we want to print the 
						  # all of the values in the columns

print('E). Write an R while and for loop that match each other in number of')
print('iterations, printing out "Here I am"')

n <- 5
while (n > 0 && n <= 5) {
	n <- n - 1
	print("(while-loop) Here I am")
}

elems <- c(1:5)
for (n in elems) {
	print("(for-loop) Here I am")
}