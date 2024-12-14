# Sets Exercises: Level 1

# Initialize the set
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

# 1. Find the length of the set it_companies
print("Length of it_companies:", len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print("After adding Twitter:", it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update({"Tesla", "Spotify", "Netflix"})
print("After adding multiple companies:", it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Google")  # Can also use discard
print("After removing Google:", it_companies)

# 5. Difference between remove and discard
# - `remove`: Raises an error if the item does not exist.
# - `discard`: Does not raise an error if the item does not exist.

# Sets Exercises: Level 2

A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

# 1. Join A and B
A_union_B = A.union(B)
print("Union of A and B:", A_union_B)

# 2. Find A intersection B
A_intersection_B = A.intersection(B)
print("Intersection of A and B:", A_intersection_B)

# 3. Is A subset of B
is_subset = A.issubset(B)
print("Is A subset of B?", is_subset)

# 4. Are A and B disjoint sets
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint?", are_disjoint)

# 5. Join A with B and B with A
A_with_B = A.union(B)
B_with_A = B.union(A)
print("A joined with B:", A_with_B)
print("B joined with A:", B_with_A)

# 6. Symmetric difference between A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetric_difference)

# 7. Delete the sets completely
del A, B

# Sets Exercises: Level 3

# 1. Convert the ages to a set and compare the length of the list and the set
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Length of the list:", len(ages))
print("Length of the set:", len(ages_set))
print("Is the list longer than the set?", len(ages) > len(ages_set))

# 2. Explain the difference between string, list, tuple, and set
# - **String**: An immutable sequence of characters.
# - **List**: A mutable, ordered collection of items.
# - **Tuple**: An immutable, ordered collection of items.
# - **Set**: An unordered, mutable collection of unique items.

# 3. Find unique words in a sentence
sentence = "I am a teacher and I love to inspire and teach people."
unique_words = set(sentence.split())
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
