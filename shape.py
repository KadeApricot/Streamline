from typing import Self, TYPE_CHECKING

if TYPE_CHECKING:
    import entity as entity
    import hitbox as hitbox

import component as component

class Shape(component.Component):
    def __init__(self, offset : tuple[float, float], objects : list[entity.Entity] = []):
        super().__init__()
        self.offset = offset
        self.objects = objects

    def get_mtv(self, other : Self):
        raise NotImplementedError()

    def get_mtv_multi(self):
        mtvs = []
        for obj in self.objects:
            if obj is not self and (hitbox_comp := obj.get_component(hitbox.Hitbox)):
                for shape in hitbox_comp.shapes:
                    if shape is not self:
                        mtv = self.get_mtv(shape)
                        if mtv is not None:
                            mtvs.append(mtv)
        if len(mtvs) == 0:
            return None
        return (sum(mtv[0] for mtv in mtvs) / len(mtvs), sum(mtv[1] for mtv in mtvs) / len(mtvs))

    def tick(self, delta : float):
        if (transform := self.entity.get_component('Transform')) and (mtv := self.get_mtv_multi()):
            transform.position = (transform.position[0] + mtv[0], transform.position[1] + mtv[1])