#!/usr/bin/env rscript

# Takes in two variables (one for numbers and one for text arguments), and 
# then checks if the first argument is greater than 100, it prints out "pass", 
# if less than 100, it prints out "fail", if equal to 100 (print out any text 
# of your choice) and if text, prints out "invalid". 

# For the second argument if 
# it is text it prints out "valid", if it is not text it does nothing. Than run 
# the function once with any choice of text, number input (examples below). 
# Note you might need to use two separate evaluation paths. Also despite the 
# first argument being intended for numbers (one could accidentally pass text), 
# for the second argument it is intended for text (one could accidently pass numbers).

## First Argument
first <- function(a) {
	# `as.numeric` coerces the variable `a` into a number, 
	# however when a does not hold a string that represents a number 
	# it is converted to `NA` and it raises a warning. After we have `NA` 
	# we use `is.na` to deteremine whether the value is `NA` or no, if it is, 
	# then exit early.
	#
	# suppressWarnings simply removes the warning that is raised by `as.numeric`
	# because in this scenario we know that there's a chance that the value is not
	#  valid number.
	# 
	if (suppressWarnings(is.na(as.numeric(a)))) {
		return("invalid")
	}

	if (a > 100) {
		"pass"
	} else if (a == 100) {
		"nice!"
	} else {
		"fail"
	}
}

## Second argument
second <- function(b) {
	if (typeof(b) == "character") {
		return("valid")
	}
	NULL
}

## TESTING

test <- function(a, b) {
	ar <- first(a)
	br <- second(b)
	if (is.null(br)) {
		print(ar)
	} else {
		print(sprintf("%s, %s", ar, br))
	}
}

test(15, "foobar")
test(15, 28)
test("foobar", 28)
test("foobar", "foobar")