# String characters ka collection hota hai.
# String immutable hota hai.
name = "PNINFOSYS"


print(name[0])
print(name[1])

# name[0]="J"
# print(name)  # TypeError: 'str' object does not support item assignment

name = name + "Softwares"
print(name)   # Concatenation


# Slicing
print(name[0:4])
print(name[4:7])
print(name[:])  # All characters
print(name[:7]) # First 7 characters
print(name[4:]) # From index 4 to end
print(name[-3:]) # Last 3 characters
print(name[::-1]) # Reverse the string
print(name[0:9]) # From index 0 to last 2 characters



# Useful String Methods
print(len(name)) 
print(name.upper()) # Convert to uppercase
print(name.lower()) # Convert to lowercase
print(name.count("N")) # Count occurrences of a character
print(name.find("N")) # Find the index of a character
print(name.replace("N", "X")) # Replace a character
print(name.strip()) # Remove leading/trailing whitespace
print(name.split()) # Split the string into a list
print(name.join()) # Join a list into a string
print(name.title()) # Convert to title case
print(name.capitalize())
