#checking and returning duplicate values in a list
values_list = ["a", "b", "a", "c", "d", "e", "f", "b"]

duplicate_values = []

for value in values_list:
  if values_list.count(value) > 1:
    if value not in duplicate_values:
      duplicate_values.append(value)

print(duplicate_values)
