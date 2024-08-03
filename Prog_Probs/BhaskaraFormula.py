def bhaskara_formula(a, b, c):
    discriminant = (b**2) - (4*a*c)
    if discriminant < 0 or 2*a == 0:
        return "Impossible to calculate"
    else:
        root1 = ((-abs(b)) + (discriminant ** 0.5)) / (2 * a)
        root2 = ((-abs(b)) - (discriminant ** 0.5)) / (2 * a)
    return f"R1 = {root1}\nR2 = {root2}"


print(bhaskara_formula(10.0, 20.1, 5.1))