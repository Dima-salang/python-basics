stars = ["Sun", "Aldebaran", "Pollux", "Polaris", "UY Scuti", "Sun"]

# to count the occurences of a substring.
print(stars.count("Sun"))

# to append an element to the end of a list.
stars.append("Orion")
print(stars)

# to find the index within a list.
print(stars.index("Aldebaran"))

# to reverse the ordering within the list.
stars.reverse()
print(stars)

# to sort the list.
stars.sort()
print(stars)

# to pop the last element and return it.
print(stars.pop())

#  remove an element.
stars.remove("Pollux")
print(stars)

# to insert an element in a given position. insert(index, element)
stars.insert(0, "Nova")
print(stars)

# to copy a list.
stars_2 = stars.copy()
print(stars_2)

# to clear a list.
print(stars.clear())


# deleting a whole list.
del stars[:]
print(stars)

# deleting an element using its index.
del stars_2[0]
print(stars_2)

# deleting entire variables
del stars_2
print(stars_2)  # cannot be defined.
