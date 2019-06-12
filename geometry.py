import os
import numpy
import sys

def calculate_distance(coords1, coords2):# 3 sets of double quotes allows to give a description for help
    """
    This funtion has two arguments, the coordinates of two atoms. It returns the distance between atoms.
    """
    distance_x = coords1[0] - coords2[0]
    distance_y = coords1[1] - coords2[1]
    distance_z = coords1[2] - coords2[2]
    distance = numpy.sqrt(distance_x**2 + distance_y**2 + distance_z**2)
    return distance

def bond_check(distance,  minimum=0, maximum=1.5): # when variables are set equal to => default
    """
    Checks a distance to se if it is a real bond.
    """
    if distance > minimum and distance < maximum:
        return True
    return False

file_location = sys.argv[1]
H2O_file = numpy.genfromtxt(fname=file_location, skip_header = 2, dtype='unicode')#read waterfile and skip the 2 first lines
symbols = H2O_file[:,0]
coordinates = H2O_file[:,1:]
coordinates = coordinates.astype(numpy.float)#change coordinates from str to float
num_atoms = len(symbols)
distance = 0
max_bond_length = 1.5
for num1 in range(0, num_atoms):
    for num2 in range(0, num_atoms):
        if num2 > num1:
            distance = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_check(distance):
                print(F'{symbols[num1]} to {symbols[num2]} : {distance:.3f}')
