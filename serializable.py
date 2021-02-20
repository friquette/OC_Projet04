""" Module containing the Serializable class"""


class Serializable:
    """ This is a factory class

    Creates the properties of an object from the property_to_serialize and the params.
    It contains 1 method:
    serialize: serialize each property of the property_to_serialize list. Uses the _pod if it exists.

    Parameters:
        property_to_serialize: list of properties corresponding to the dictionary keys.
        **params: the dictionary used to create the object.

    """
    def __init__(self, property_to_serialize: list, **params):
        self.property_to_serialize = property_to_serialize
        self.params = params
        incorrect_values = set()

        for property in self.property_to_serialize:
            try:
                setattr(self, property, params[property] if property in params else None)
            except ValueError:
                incorrect_values.add(property)

        if incorrect_values:
            raise ValueError(f"Paramètres de model player incorrects: {incorrect_values}")

    def serialize(self):
        for i in range(len(self.property_to_serialize)):
            my_property = self.property_to_serialize[i]

            if hasattr(self, f"{my_property}_pod"):
                self.params[my_property] = getattr(self, f"{my_property}_pod")
