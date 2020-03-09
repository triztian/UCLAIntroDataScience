from apyori import apriori 
from enum import IntEnum

# Define the enumerations, the library requires items to be sortable, hence we 
# use an `IntEnum`
Item = IntEnum('Item', 'A B C')

transactions = frozenset({
	frozenset({Item.A, Item.B, Item.C}),
	frozenset({Item.A, Item.B}),
	frozenset({Item.A, Item.C}),
	frozenset({Item.A}),
})

rules = list(apriori(transactions))

print('Rule Count:', len(rules))
for r in list(rules):
	print(','.join(map(str, r.items)), 'Support:', r.support)