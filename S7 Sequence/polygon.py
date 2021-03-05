from math import sin, cos, pi


class Polygon:
    def __init__(self, nedges: int, circumradius: float) -> None:
        self.nedges = nedges
        self.vertices = nedges
        self.circumradius = circumradius

        self.interior_angle = (self.nedges-2) * (180/self.nedges)
        self.edge_length = 2 * self.circumradius * sin(pi/self.nedges)
        self.apothem = cos(pi/self.nedges)
        self.area = (self.nedges * self.edge_length * self.apothem) / 2
        self.perimeter = self.nedges * self.edge_length
        self.efficiency =self.area/self.perimeter 

    def __repr__(self):
        return 'Polygon(nedges=%s, circumradius=%s)' % (self.nedges, self.circumradius)

    
    def eq(self, other_polygon):
        return self.nedges == other_polygon.nedges and self.circumradius == other_polygon.circumradius

    def gt(self, other_polygon):
        return self.nedges > other_polygon.nedges
