print("■  len(str)")
test_string = "The siege tower will guide us into battle! "
print(f"{test_string}: {len(test_string)} Zeichen lang\n")

print("■  str[index]")
print(f"{test_string[36]}, {test_string[-1]}\n")

print("■  str[start:end] / str[start:end:step]")
print(f"Last Word: {test_string[-8:-1]}")
print(f"Reversed: {test_string[::-1]}\n")

print("■  str.lower() / str.upper()")
print(f"lower: {str.lower(test_string)}")
print(f"upper: {str.upper(test_string)}\n")

print("■  str.strip()")
print(f"stripped: {str.strip(test_string)}")