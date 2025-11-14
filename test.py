class ParentA:
    def method_a(self):
        return "Method A from Parent - A"


class ParentB:
    def method_a(self):
        return "Method A from Parent - B"


class Child(ParentA, ParentB):
    pass


def test_method_resolution_order():
    child = Child()
    print(child.method_a())


test_method_resolution_order()
