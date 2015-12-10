class AttrDict(dict):

    """ A dict that allows object-like value access syntax. """

    def __init__(self, new_dict=None):
        dict.__init__(self)
        if new_dict:
            self.update(new_dict)

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, key, value):
        self.update({key: value})