from dataclasses import dataclass


class MagicList(list):
    def __init__(self, cls_type=None):
        self.cls_type = cls_type

    def __getitem__(self, key):
        if self.cls_type is not None and key == len(self):
            self.append(self.cls_type())

        return list.__getitem__(self, key)

    def __setitem__(self, key, value):
        print(f"AAA len(self): {len(self)}")

        if key == len(self):
            # if self.cls_type is not None:
            #     value = self.clstype()

            return self.append(value)

        else:
            return list.__setitem__(self, key, value)

# a = MagicList()
# a[0] = 12
# a.append(3)
# a.append(9)
# print(a)
# a[0]=7
# print(a)

# TODO: add tests

@dataclass
class Person:
    age: int = 1

b = MagicList(cls_type=Person)
b[0].age = 5
b[1].age = 8
# b[3].age = 4 # should raise exception
print(b)

