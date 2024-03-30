###################################################################################
# Finding cube root using bisection search method
# MIT 6.0001 problem (lecture 3 in class problem) [Available in mit ocw website]
###################################################################################


# Asking user input
cube = float(input("Enter cubic number : "))

# Accuracy
epsilon = 0.01

num_guesses = 0

# Changing -cube to cube for convenience
org_cube = 0

if cube < 0:
    org_cube = cube
    cube = abs(cube)

# Initial value setting for guess
low = 0
high = cube

guess = (low+high) / 2.0


# Handling cube = 0 seperately
if cube == 0:
    print(f"Cube root of {int(cube)} is 0")

# For positive cubes
elif cube > 1:
    while (abs(guess**3 - cube)>=epsilon and guess <= cube):
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        num_guesses += 1

        # No more than 2500 guesses
        if num_guesses > 2500:
            print("Failed to find cube root !!")
            break

# For negative cubes
else:
    low = cube
    high = 1
    guess = (low + high) / 2.0
    while (abs(guess**3 - cube)>=epsilon and guess <= 1):
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        num_guesses += 1

        # No more than 2500 guesses
        if num_guesses > 2500:
            print("Failed to find cube root !!")
            break            


# Final value printing
if cube != 0:
    if org_cube < 0:
        guess *= -1
        print(f"Cube root of {org_cube} is : {guess}")
    else:
        print(f"Cube root of {cube} is : {guess}")
    

