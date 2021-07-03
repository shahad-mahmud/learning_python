is_found = False

numbers = [1, 2, 3, 45, 64, 23, 89, -56, -32, 4, 56, 8, 23, 56546, -34543]
key = -64

for idx, value in enumerate(numbers):
    if value == key:
        is_found = True
        break

if is_found:
    print(f"Found {key}")
else:
    print(f"{key} not found in the list")

