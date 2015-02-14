from icoolnamelistcontainer import *


class Ncv(ICoolNameListContainer):
    allowed_enclosed_commands = []

    command_params = {}

    def __init__(self, **kwargs):
        ICoolObject.__init__(self, kwargs)
        Container.__init__(self)

    def __setattr__(self, name, value):
        Container.__setattr__(self, name, value)