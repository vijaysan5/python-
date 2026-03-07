# Set Methods
"""
add()	 	            Adds an element to the set
clear()	 	            Removes all the elements from the set
copy()	 	            Returns a copy of the set
difference()	    -	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	        Remove the specified item
intersection()	    &	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	    Returns whether two sets have a intersection or not
issubset()	        <=	Returns True if all items of this set is present in another set
 	                <	Returns True if all items of this set is present in another, larger set
issuperset()	    >=	Returns True if all items of another set is present in this set
 	                >	Returns True if all items of another, smaller set is present in this set
pop()	 	        Removes an element from the set
remove()	 	    Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	            |	Return a set containing the union of sets
update()	        |=	Update the set with the union of this set and others"""

## frozenset
# Unlike sets, elements cannot be added or removed from a frozenset.

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))   

# Frozenset Methods
# copy()	 	        Returns a shallow copy	
# difference()	    -	Returns a new frozenset with the difference	
# intersection()	&	Returns a new frozenset with the intersection	
# isdisjoint()	 	    Returns whether two frozensets have an intersection	
# issubset()	<= / <	Returns True if this frozenset is a (proper) subset of another	
# issuperset()	>= / >	Returns True if this frozenset is a (proper) superset of another	
# symmetric_difference()	^	Returns a new frozenset with the symmetric differences	
# union()	        |	Returns a new frozenset containing the union


# Dictionary Methods
""" 
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary """


