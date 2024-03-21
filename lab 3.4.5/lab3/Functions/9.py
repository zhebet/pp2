def sphere_volume(radius):
    volume = (4/3) * 3.14159 * radius ** 3
    return volume


radius = float(input(""))
print(sphere_volume(radius))
