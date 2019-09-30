def sqrt(x):
    # Initial guess

    z = 1.0
    # Keep getting a better estimate for the square root
    # of x, until you are within two decimal places
    while abs(z * z - x) >= 0.01:
        # get better approximation for square root
        z -= (z*z -x) / (2*z)   
    return z


#Calculate the square root of 8, print.
z = sqrt(98)
print(z)

print(z*z)
