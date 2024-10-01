from _math_functions import ffi, lib

# Call the compiled C functions
result_add = lib.add(10, 20)
result_multiply = lib.multiply(5, 6)

print(f"Add: 10 + 20 = {result_add}")
print(f"Multiply: 5 * 6 = {result_multiply}")