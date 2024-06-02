class Validate:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целым числом.")
        setattr(instance, self.private_name, value)


class Point3D:
    x = Validate()
    y = Validate()
    z = Validate()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__)
