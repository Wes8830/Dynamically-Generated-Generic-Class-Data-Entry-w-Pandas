class GenericORM:
    """
    This is a dynamic class that allows you to define key value pairs,
    at runtime
    """

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class BasicORM:
    """
    So is this.
    """
    pass