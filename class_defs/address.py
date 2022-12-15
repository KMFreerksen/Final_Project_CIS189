class InvalidStreetNumberException(Exception):
    """InvalidStreetNumberException is derived class of Exception base class"""
    pass


class InvalidStreetNameException(Exception):
    """InvalidStreetNameException is derived class of Exception base class"""
    pass


class InvalidStreetTypeException(Exception):
    """InvalidStreetTypeException is derived class of Exception base class"""
    pass


class InvalidCityException(Exception):
    """InvalidCityException is derived class of Exception base class"""
    pass


class InvalidStateException(Exception):
    """InvalidStateException is derived class of Exception base class"""
    pass


class InvalidZipException(Exception):
    """InvalidZipException is derived class of Exception base class"""
    pass


class InvalidApartmentException(Exception):
    """InvalidAptException is derived class of Exception base class"""
    pass


class address:
    """Address class for US addresses"""

    def __init__(self, st_number, st_name, st_type, city, state, zipcode, apt_num=''):
        alpha_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'- ")
        alphanumeric_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'1234567890- ")
        numeric_characters = set("1234567890-")
        street_type_list = ['aly', 'Alley', 'ave', 'Avenue', 'blv', 'Boulevard', 'blvd', 'Boulevard', 'cir',
                            'Circle', 'ct', 'Court', 'cv', 'Cove', 'cyn', 'Canyon', 'dr', 'Drive', 'expy',
                            'Expressway', 'hwy', 'Highway', 'ln', 'Lane', 'pkwy', 'Parkway', 'pl', 'Place',
                            'pt', 'Point', 'rd', 'Road', 'sq', 'Square', 'st', 'Street', 'ter', 'Terrace',
                            'tr', 'Trail', 'trl', 'Trail', 'wy', 'Way']
        states = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL',
                  'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
                  'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
                  'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
        if not (numeric_characters.issuperset(st_number)):
            raise InvalidStreetNumberException
        if not (alphanumeric_characters.issuperset(st_name)):
            raise InvalidStreetNameException
        if not (street_type_list.__contains__(st_type)):
            raise InvalidStreetTypeException
        if not (alphanumeric_characters.issuperset(apt_num)):
            raise InvalidApartmentException
        if not (alpha_characters.issuperset(city)):
            raise InvalidCityException
        if not (states.__contains__(state)):
            raise InvalidStateException
        if not (numeric_characters.issuperset(zipcode) and (len(zipcode) == 5 or len(zipcode) == 10)):
            raise InvalidZipException

        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zipcode

    def display(self):
        return (self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
                + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)


# Driver
addy1 = address('123', 'Main', 'Street', 'Small Town', 'IA', '11111')
print(addy1.display())

# Invalid street number
try:
    addy2 = address('abc', 'Main', 'Street', 'Small Town', 'IA', '11111')
except InvalidStreetNumberException:
    print("Invalid Street Number, customer not created")

# Invalid street name
try:
    addy2 = address('123', '###', 'Street', 'Small Town', 'IA', '11111')
except InvalidStreetNameException:
    print("Invalid Street Name, customer not created")

# Invalid street type
try:
    addy2 = address('123', 'Main', 'Teleporter', 'Small Town', 'IA', '11111')
except InvalidStreetTypeException:
    print("Invalid Street Type, customer not created")

# Invalid city
try:
    addy2 = address('123', 'Main', 'Street', '###', 'IA', '11111')
except InvalidCityException:
    print("Invalid City, customer not created")

# Invalid state
try:
    addy2 = address('123', 'Main', 'Street', 'Small Town', 'frankfurter', '11111')
except InvalidStateException:
    print("Invalid State, customer not created")

# Invalid zip
try:
    addy2 = address('123', 'Main', 'Street', 'Small Town', 'IA', 'omicron')
except InvalidZipException:
    print("Invalid Zip Code, customer not created")

del addy1
