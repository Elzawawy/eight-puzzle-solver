import math

def manhattan_distance(point1, point2):
    """ It is the sum of absolute values of differences in the point 1's x and y coordinates and the
        point 2's x and y coordinates respectively """
    return abs(point1.point[0] - point2.point[0]) + abs(point1.point[1]-point2.point[0])

def eculidean_distance(point1,point2):
    return math.sqrt(math.pow(point1.point[0] - point2.point[0],2) + math.pow(point1.point[1]-point2.point[0],2))
