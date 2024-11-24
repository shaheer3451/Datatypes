# Define the variables
a = 10
b = -10

# Number of positions to shift
shift = 2

# Apply left and right shifts on 'a'
a_left_shift = a << shift  # Left shift multiplies by 4 (2^2)
a_right_shift = a >> shift  # Right shift divides by 4 (2^2)

# Apply left and right shifts on 'b'
b_left_shift = b << shift  # Left shift multiplies by 4 (but keeps the negative sign)
b_right_shift = b >> shift  # Right shift divides by 4 (negative stays negative)

# Print the results with explanation
print(f"Original a = {a}, Left Shift (a << {shift}) = {a_left_shift}, Right Shift (a >> {shift}) = {a_right_shift}")
print(f"Original b = {b}, Left Shift (b << {shift}) = {b_left_shift}, Right Shift (b >> {shift}) = {b_right_shift}")
