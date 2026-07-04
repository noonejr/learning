"""
Given a temperature in Fahrenheit, return the temperature in Celsius
"""

# Ask for a temperature in Fahrenheit
temp_in_far_string = input("Please enter temperature in Fahrenheit: ")

temp_in_far = int(temp_in_far_string)

# Calculate it in Celsius
temp_in_cel = ((temp_in_far - 32) * 5)/9

# Tell the user what it is
print(temp_in_cel)