from cffi import FFI

ffi = FFI()

# Load the shared library
lib = ffi.dlopen("./libmath_functions.dylib")

# Declare the function signatures
ffi.cdef("""
    int add(int a, int b);
    int multiply(int a, int b);
""")

# Call the functions from the library
result_add = lib.add(10, 20)
result_multiply = lib.multiply(5, 6)

print(f"Add: 10 + 20 = {result_add}")
print(f"Multiply: 5 * 6 = {result_multiply}")