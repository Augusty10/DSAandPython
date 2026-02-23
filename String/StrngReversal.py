
def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str
# Example usage 
input_str=" Hello, World ! "
reversed_str=reverse_string(input_str)
print(f"Original string: {input_str}")
print(f"Reversed string: {reversed_str}")

