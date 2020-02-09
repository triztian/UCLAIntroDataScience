# Module 2b
# Author: Tristian Azuara
# Email: tristian.azuara@gmail.com
# UCLA: Introduction to Data Science
#

print('# A) Variables, types and casting')
# Unlike other languages like javascript, python does not implicitly cast
# objects into strings when using the '+' operator with strings.
# One must cast any non-str objects into strings
a = 1
b = 'one'
r = str(a) + b

print(r)

print("""# B) Create a list of integers, strings, i.e. someList = [3, ' S', 'B', 21]
# Separate the list into one of only strings, and one of only intergers.""")

mix_list = [3, 'S', 'B', 21, 99, 78, 'aa', 'xx']

def make_type_filter(typ):
	"""Creates a filter for the provided type. It will return `True` if the
		element matches the provided type.
	"""
	return lambda x: type(x) is typ

# We use the `filter` function and a function that creates a filter to be applied
# to each element of the list.
ints = list(filter(make_type_filter(int), mix_list))

# We use a list comprehension along with a filter expression that checks for the appropriate
# types. For this particular use case the comprehension is far easier to read.
strs = [x for x in mix_list if type(x) is str]

print(ints)
print(strs)

print("""C) Compare and contrast the data structure from the official Python list of 
# data structures (i.e. tuples, dicts, lists), i.e. Tuples are the ONLY 
# immutable data structure (there are lists, tuples, sets, dictionaries)""")

# Lists
# Lists allow us to have a heterogenous sequence of elements, elements 
# can be repeated.
# Lists can be combined, extended, sliced `[:]`, traversed in for-loops and 
# elements can be accessed by indexes in square brackets `my_list[3]`
my_list = ['1', 99, 84, 2.8]
print(my_list)

# Sets
# Sets like lists can hold a heterogenous _collection_ of elements, however 
# the order of the elements in a set is not guaranteed, a set by definition is 
# an unordered collection (like dictionaries) a `Set` also does not allow for 
# duplicate elements, set elements are not accessed by index set elements must
# be hashable and support some of the mathematical set operations.

my_set = {1,2,2,2,2,2,1,3, 'a', 'a'}
empty_set = set() 
print(my_set) # {1, 2, 3, 'a'}, order may change

# Dictionaries
# A dictionary defines a mapping of keys to values. The key element must be 
# hashable (a unique identity can derived for it), the value element doesn't 
# have to be hashable.
# A dictionary value can be a complex data structure such as a class or even 
# another dictionary, set, list or tuple
my_dict = {'a': 99, 'b': 42, 'c': 'string!', 99: [1, 2, 3], 88: {1,2,2,2,3}}
empty_dict = {}

# Tuples
# A tuple is an immutable data structure in Python, it is simply an ordered collection
# of values, because tuples are _immutable_ their contents cannot be reassigned 
# after they've been created (however, if the values happen to be classes the can mutate
# their internal state). Also unlike lists or dictionaries, tuples can be used 
# as dictionary keys because of their immutability
my_tuple = (1, 2, 3, 'a', 'b', 'c')
empty_tuple = ()

print("""# D) Compare and contrast some Python specialized data types/objects 
# (please select at least a minimum of 2 items, i.e. datetime, collections)""")

# Datetime, Timedelta
# Manupilating dates and computing differences between them is a common task 
# when analyzing data, it's also used for calculating deadlines, time elapsed
# and more specifically to plot time series graphs.

# Datetime is provided by the datetime package, it's imported like so:
#
#		from datetime import datetime
#
# One may be tempted to simply represent a date and time as tuples, dictionaries, 
# lists or as a custom class, however the Python3 standard library already
# includes functions and methods that take care of timezone information, 
# translation between timezones, computation and addition or subtraction to date
# not no mention handling many of the nuances of our date and time systems (such
# as daylight savings, formatting, localization, etc)
#
# Subtracting ('-' operator) 2 dates yields a `timedelta` object which contains 
# the difference in days, seconds and years between such dates, timedelta objects
# can be added ('+' operator) to other datetime and timedelta objects to produce
# new dates and timedelta objects.

from datetime import datetime
now = datetime.now() # current date and time with the computer's timezone
# Months are 1-based (unlike list or tuple indexes)
b = datetime(2020, 2, 3) # Last Monday
a = datetime(2020, 2, 10) # Next Monday

diff = a - b # Time delta
fortnight = diff * 2 # or diff + diff
b + fortnight # Payday!

# Enum
# An enumeration is a way to define a finite set of values that are different
# instances or occurrences within a category.
# It defines unique constant symbols that can be compared and iterated. For example
# usually one defines a list of operations modes to global variables, instead
# An enum structure could be used that would provide iteration, value protection (
# by making it a constant) and it'd also improve readability. Because Enums
# are hashable, they can be used as dictionary keys

from enum import Enum
class OperationMode(Enum):
	PRODUCTION = 1
	DEBUG = 2

print(OperationMode.PRODUCTION)

print("""# E) Write a function that separates out the negative and positive integers in 
# a list, i.e. someList = [3,-3, 4, -5]""")

def split_sign(numbers, exclude_zero=False):
	"""Splits a list of numbers by their sign"""
	positive = []
	negative = []

	for x in numbers:
		if x < 0:
			negative.append(x)
		elif x > 0:
			positive.append(x)
		else: # 0 goes on both?, or it could be excluded
			if not exclude_zero:
				negative.append(x)
				positive.append(x)

	return (positive, negative)

numbers = [1, 2, 3, 4, -0, 0, -2, -4, 5, 2, -1, -56, 9, -33]
pos, neg = split_sign(numbers)

print(neg)
print(pos)