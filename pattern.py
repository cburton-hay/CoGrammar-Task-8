# Creating a pattern using * and increasing and decreasing the ammount.

for x in range(1, 10): # The pattern goes over 9 lines
    if x <=5: 
        pattern = x * "*" # Allows the number of stars to increase within the first 5 lines of the pattern.
    else:
        pattern = "*" * (10 - x) # Using number bonds to 10 means that the higher x value means it takes away more and therefore decrease how many stars are in the pattern.
    print(pattern)
