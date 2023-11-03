import ephem

jupiter = ephem.Jupiter()

jupiter.compute("1230/01/01")

distance_au_units = jupiter.sun_distance
distance_km = distance_au_units * 149597870.691
print(distance_km)
