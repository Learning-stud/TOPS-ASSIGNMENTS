import math

def degree_to_radian(degree):
    """Convert degrees to radians."""
    return degree * (math.pi / 180)

result = degree_to_radian(90)
print("90 degrees in radians:", result)