vegetables = set()

vegetables.add("potato")
vegetables.add("carrot")
vegetables.add("lettuce")
vegetables.add("tomato")

fruits = set()
fruits.update(["tomato","apple","orange"])
# removes all duplicates from both sets (keeps only one duplicate)
fruits_and_vegetables_union = vegetables.union(fruits)
print(fruits_and_vegetables_union)

# gets the common elements from both sets (get back the duplicate)
fruits_and_vegetables_intersection = vegetables.intersection(fruits)
print(fruits_and_vegetables_intersection)

# gives us all of the items which only feature in one of the sets (removes all duplicates keeping none)
fruits_and_vegetables_symmetric_diff = vegetables.symmetric_difference(fruits)
print(fruits_and_vegetables_symmetric_diff)
