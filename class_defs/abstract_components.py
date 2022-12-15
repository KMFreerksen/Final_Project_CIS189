import decimal
from abc import ABC, abstractmethod, abstractproperty


class InvalidQuantityException(Exception):
    """InvalidNameException is derived class of Exception base class"""
    pass


class component(ABC):
    @abstractmethod
    def distributor(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def quantity(self):
        pass

    @abstractmethod
    def get_stock_value(self):
        pass


class Topper(component):
    def __init__(self, name, dist, cost, quant, height):
        decimal_characters = set("1234567890-.")
        if not isinstance(name, str):
            raise TypeError('name is not a string value')
        if not isinstance(dist, str):
            raise TypeError('distributor is not a string value')
        if not decimal_characters.issuperset(str(cost)):
            raise TypeError('cost is not a decimal')
        if not (isinstance(quant, int) and (quant >= 0)):
            raise InvalidQuantityException
        if not decimal_characters.issuperset(str(height)):
            raise ValueError
        self._name = name
        self._distributor = dist
        self._cost = cost
        self._quantity = quant
        self.height = height

    def __str__(self):
        return self.type() + "Name: " + self._name + " Quantity: " + str(self._quantity) + " Height: " + str(
            self.height)

    def display(self):
        return self.type() + "Name: " + self._name

    def type(self):
        return 'Topper - '

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def height(self):
        return self.height

    def set_height(self, value):
        decimal_characters = set("1234567890-.")
        if not decimal_characters.issuperset(value):
            raise ValueError
        self.height = value

    def get_stock_value(self):
        return self.cost * self.quantity


class Column(component):
    def __init__(self, name, dist, cost, quant, color, shape):
        decimal_characters = set("1234567890-.")
        if not isinstance(name, str):
            raise TypeError('name is not a string value')
        if not isinstance(dist, str):
            raise TypeError('distributor is not a string value')
        if not decimal_characters.issuperset(str(cost)):
            raise TypeError('cost is not a decimal')
        if not (isinstance(quant, int) and (quant >= 0)):
            raise InvalidQuantityException
        shapes = ['round', 'rectangle', 'oval']
        colors = ['blue', 'red', 'green', 'silver', 'gold', 'orange', 'purple', 'black', 'pink', 'maroon']
        if not shapes.__contains__(shape):
            raise ValueError
        if not colors.__contains__(color):
            raise ValueError
        self._name = name
        self._distributor = dist
        self._cost = cost
        self._quantity = quant
        self.color = color
        self.shape = shape

    def __str__(self):
        return self.type() + "Name: " + self._name + " Quantity: " + str(
            self._quantity) + " (" + self.shape + " " + self.color + ")"

    def display(self):
        return self.type() + "Name: " + self._name + " (" + self.shape + " " + self.color + ")"

    def type(self):
        return 'Column - '

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value

    def color(self):
        return self.color

    def set_color(self, value):
        colors = ['blue', 'red', 'green', 'silver', 'gold', 'orange', 'purple', 'black', 'pink', 'maroon']
        if not colors.__contains__(value):
            raise ValueError
        self.color = value

    def shape(self):
        return self.shape

    def set_shape(self, value):
        shapes = ['round', 'rectangle', 'oval']
        if not shapes.__contains__(value):
            raise ValueError
        self.shape = value

    def get_stock_value(self):
        return self.cost * self.quantity


class MarbleBase(component):
    def __init__(self, name, dist, cost, quant):
        decimal_characters = set("1234567890-.")
        if not isinstance(name, str):
            raise TypeError('name is not a string value')
        if not isinstance(dist, str):
            raise TypeError('distributor is not a string value')
        if not decimal_characters.issuperset(str(cost)):
            raise TypeError('cost is not a decimal')
        if not (isinstance(quant, int) and (quant >= 0)):
            raise InvalidQuantityException
        self._name = name
        self._distributor = dist
        self._cost = cost
        self._quantity = quant

    def __str__(self):
        return self.type() + "Name: " + self._name + " Quantity: " + str(self._quantity)

    def display(self):
        return self.type() + "Name: " + self._name

    def type(self):
        return 'Marble Base - '

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value

    def get_stock_value(self):
        return self.cost * self.quantity


class Hardware(component):
    def __init__(self, name, dist, cost, quant):
        decimal_characters = set("1234567890-.")
        if not isinstance(name, str):
            raise TypeError('name is not a string value')
        if not isinstance(dist, str):
            raise TypeError('distributor is not a string value')
        if not decimal_characters.issuperset(str(cost)):
            raise TypeError('cost is not a decimal')
        if not (isinstance(quant, int) and (quant >= 0)):
            raise InvalidQuantityException
        self._name = name
        self._distributor = dist
        self._cost = cost
        self._quantity = quant

    def __str__(self):
        return self.type() + "Name: " + self._name + " Quantity: " + str(self._quantity)

    def display(self):
        return self.type() + "Name: " + self._name

    def type(self):
        return 'Hardware - '

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value

    def get_stock_value(self):
        return self.cost * self.quantity


class Rods(component):
    def __init__(self, name, dist, cost, quant, len, half=False):
        decimal_characters = set("1234567890-.")
        if not isinstance(name, str):
            raise TypeError('name is not a string value')
        if not isinstance(dist, str):
            raise TypeError('distributor is not a string value')
        if not decimal_characters.issuperset(str(cost)):
            raise TypeError('cost is not a decimal')
        if not (isinstance(quant, int) and (quant >= 0)):
            raise InvalidQuantityException
        if not isinstance(len, int):
            raise TypeError
        if not isinstance(half, bool):
            raise TypeError
        self._name = name
        self._distributor = dist
        self._cost = cost
        self._quantity = quant
        self._length = len
        self._half = half

    def __str__(self):
        return self.type() + "Name: " + self._name + " Quantity: " + str(self._quantity)

    def display(self):
        return self.type() + "Name: " + self._name

    def type(self):
        return 'Rod - '

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def distributor(self):
        return self._distributor

    @distributor.setter
    def distributor(self, value):
        self._distributor = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = value

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value

    def length(self):
        if self._half:
            return self._length + .5
        else:
            return self.length

    def set_length(self, len, half=False):
        if not isinstance(len, int):
            raise TypeError
        if not isinstance((half, bool)):
            raise TypeError

    def get_stock_value(self):
        return self.cost * self.quantity


# Driver

# Initialize Valid Constructors
top1 = Topper('Chess Star', 'jds', 1.25, 100, 3.75)
top2 = Topper('Star w Sticker', 'jds', 1.09, 100, 4.25)

column1 = Column('galaxy column', 'jds', 0.29, 2400, 'red', 'round')
column2 = Column('fire column', 'jds', 0.22, 2400, 'gold', 'round')
column3 = Column('galaxy column', 'jds', 0.38, 2400, 'red', 'rectangle')
column4 = Column('fire column', 'jds', 0.36, 2400, 'gold', 'rectangle')

base1 = MarbleBase('2x3 single base', 'jds', 0.54, 100)
base2 = MarbleBase('2x4 single base', 'jds', 0.69, 100)


hexnut = Hardware('flanged hexnut', 'jds', 0.05, 5000)
checkring = Hardware('check ring', 'jds', 0.02, 5000)
ferrule = Hardware('ferrule 3/4"', 'jds', 0.07, 1000)

rod1 = Rods('4.5" Rod', 'jds', 0.14, 500, 4, True)
rod2 = Rods('5" Rod', 'jds', 0.14, 500, 5)
rod3 = Rods('5.5" Rod', 'jds', 0.14, 500, 5, True)
rod4 = Rods('5" Rod', 'jds', 0.14, 500, 6)
rod5 = Rods('6.5" Rod', 'jds', 0.14, 500, 6, True)
rod6 = Rods('5" Rod', 'jds', 0.14, 500, 7)
rod7 = Rods('7.5" Rod', 'jds', 0.14, 500, 7, True)
rod8 = Rods('5" Rod', 'jds', 0.14, 500, 8)
rod9 = Rods('8.5" Rod', 'jds', 0.14, 500, 8, True)
