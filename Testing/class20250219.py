def volume_cyclinder(height, radius):
    """This function calculates the volume of a cylinder"""
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume

can_radius = 1.5
can_height = 6

can_volume = volume_cyclinder(can_height, can_radius)
print(can_volume)