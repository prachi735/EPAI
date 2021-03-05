from polygon import *

class Polygon_sequence():
    def __init__(self, largest_nedge, circumradius):
        self.items = [Polygon(nedge,circumradius) for nedge in range(3,largest_nedge+1)]
        self.largest_nedge = largest_nedge
        self.circumradius = circumradius
        self.max_efficiency_polygon = self.get_max_efficiency_polygon()
        
    def __getitem__(self,key):
        if key < 0 or key >= len(self):
                raise IndexError('{} object index out of range'.format(
                    type(self).__name__))
        return self.items[key]
        
    
    def get_max_efficiency_polygon(self):
        return max(self.items, key=lambda a: a.efficiency)
    
    
    def __len__(self):
        return self.largest_nedge - 2
    
    def __repr__(self):
        return 'Polygons(largest_nedge=%s, circumradius=%s)' % (self.largest_nedge, self.circumradius)
