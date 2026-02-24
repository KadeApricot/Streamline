import shape as shape
import transform as transform

class AABB(shape.Shape):
    def __init__(self, float, w : float, h : float):
        self.w = w
        self.h = h
    
    def get_mtv(self, other : shape.Shape):
        if isinstance(other, AABB):
            transform_comp = self.entity.get_component(transform.Transform)
            other_transform_comp = other.entity.get_component(transform.Transform)
            
            dx = transform_comp.pos.x - other_transform_comp.pos.x
            px = (self.w + other.w) / 2 - abs(dx)
            if px <= 0:
                return None

            dy = transform_comp.pos.y - other_transform_comp.pos.y
            py = (self.h + other.h) / 2 - abs(dy)
            if py <= 0:
                return None

            if px < py:
                sx = 1 if dx < 0 else -1
                return (px * sx, 0)
            else:
                sy = 1 if dy < 0 else -1
                return (0, py * sy)

        return None