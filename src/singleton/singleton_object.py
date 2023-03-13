class SingletonObject(object):
    """

    we have only one class instance. if we create another class we rewrite
    a previous instance.
    """

    instance = None

    class __SingletonObject:
        def __init__(self):
            self.val = None

        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

        # the rest of the class definition will follow here, as per the previous
        # logging script

    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)