import shape as shape

class AABB(shape.Shape):
    def __init__(self, x : float, y : float, w : float, h : float):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def get_mtv(self, other : shape.Shape):
        if isinstance(other, AABB):
            dx = (self.x + self.w / 2) - (other.x + other.w / 2)
            dy = (self.y + self.h / 2) - (other.y + other.h / 2)
            combined_half_widths = (self.w + other.w) / 2
            combined_half_heights = (self.h + other.h) / 2

            if abs(dx) < combined_half_widths and abs(dy) < combined_half_heights:
                overlap_x = combined_half_widths - abs(dx)
                overlap_y = combined_half_heights - abs(dy)

                if overlap_x < overlap_y:
                    return (overlap_x if dx > 0 else -overlap_x, 0)
                else:
                    return (0, overlap_y if dy > 0 else -overlap_y)
        
        return None