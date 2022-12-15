from class_defs import abstract_components as a

class Trophy:
    def __init__(self, name, top, col, base, h, hard=[]):
        self._name = name
        self.topper = top
        self.column = col
        self.marble = base
        self.height = h
        self.hardware = hard

    def __str__(self):
        return self._name + "\n   " + self.topper.display() + " " + self.column.display() + " " + self.marble.display()

    def set_height(self, n):
        self.height = n

    def get_col_length(self):
        return self.height - self.topper.height() - 0.75

    def set_hardware(self, component):
        self.hardware.append(component)


trophy1 = Trophy('12" Round', a.top1, a.column1, a.base1, 12)
trophy2 = Trophy('14" round', a.top1, a.column1, a.base2, 14)
trophy3 = Trophy('16" round', a.top1, a.column1, a.base2, 16)
trophy4 = Trophy('12" Round', a.top2, a.column2, a.base2, 12)
trophy5 = Trophy('14" round', a.top2, a.column2, a.base2, 14)
trophy6 = Trophy('16" round', a.top2, a.column2, a.base2, 16)
