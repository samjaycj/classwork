print("----- Set Operations ------")

set_a = {10, 20, 30, 40, 50, 90}
set_b = {40, 50, 60, 70, 80}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")
print(f"Union of Set A and Set B is: {set_a.union(set_b)}")
print(f"Intersection of Set A and Set B: {set_a.intersection(set_b)}")
print(f"Difference (Set A - Set B): {set_a.difference(set_b)}")

print("\n ... List De-duplication using sets ...")
my_list = [1, 2, 2, 3, 3, 4, 5, 1, 6]
print(f"Original list with duplicates: {my_list}")
print(f"Duplicates removed by converting to set: {set(my_list)}")
print(f"Covert the set back to a list: {list(set(my_list))}")
