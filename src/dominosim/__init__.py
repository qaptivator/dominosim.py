
from enum import Enum
from typing import List

# global vars
class OBJ_TYPE(Enum):
    ORTHOGONAL_DOMINO = 'OrthogonalDomino'
    DIAGONAL_DOMINO = 'DiagonalDomino'
    FORK_DOMINO = 'ForkDomino'
    CROSSOVER = 'Crossover'
    TRIGGER = 'Trigger'

class OBJ_ROT(Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

# classes
class Object:
    def __init__(self, _type: OBJ_TYPE, x: int, y: int, rot: OBJ_ROT):
        self.type = _type
        self.x = x
        self.y = y
        self.rot = rot

class Level:
    def __init__(self, objects=None, global_delete_existing=False):
        if objects is None:
            objects = []
        self.objects = objects
        self.global_delete_existing = global_delete_existing

    def get_objects(self) -> List[Object]:
        return self.objects

    def get_object(self, obj: Object) -> Object | None:
        for [i, existing_obj] in enumerate(self.objects):
            if existing_obj.x == obj.x and existing_obj.y == obj.y and existing_obj.type == obj.type:
                return existing_obj
        return None

    def get_object_xy(self, x: int, y: int) -> Object | None:
        for [i, existing_obj] in enumerate(self.objects):
            if existing_obj.x == x and existing_obj.y == y:
                return existing_obj
        return None

    def delete_object(self, obj: Object) -> None:
        for [i, existing_obj] in enumerate(self.objects):
            if existing_obj.x == obj.x and existing_obj.y == obj.y and existing_obj.type == obj.type:
                self.objects.pop(i)
                break

    def delete_object_xy(self, x: int, y: int) -> None:
        for [i, existing_obj] in enumerate(self.objects):
            if existing_obj.x == x and existing_obj.y == y:
                self.objects.pop(i)
                break

    def add_object(self, obj: Object, delete_existing=False) -> None:
        if delete_existing or self.global_delete_existing:
            self.delete_object(obj)
        self.objects.append(obj)

    @staticmethod
    def parse(level_str: str): # -> Level, -> Self dont work here
        parts = level_str.strip().split(' ')

        objects = []
        obj_type = ''
        obj_x = 0
        obj_y = 0
        obj_rot = 0

        for [index, part] in enumerate(parts):
            var_index = index % 4
            if var_index == 0:
                obj_type = part
            elif var_index == 1:
                obj_x = int(part)
            elif var_index == 2:
                obj_y = int(part)
            elif var_index == 3:
                obj_rot = int(part) or 0
                if obj_type:
                    objects.append(Object(OBJ_TYPE(obj_type), obj_x, obj_y, OBJ_ROT(obj_rot)))

        return Level(objects)

    def stringify(self) -> str:
        return ' '.join([f'{obj.type.value} {obj.x} {obj.y} {obj.rot.value}' for obj in self.objects])