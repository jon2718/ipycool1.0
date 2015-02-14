from icoolnamelistcontainer import *
from beamtype import *


class Bmt(ICoolNameListContainer):

    allowed_enclosed_commands = ['BeamType']

    command_params = {
        'nbeamtyp': {
            'desc': '# of beam types, e.g., particles of different masses.',
            'doc': '',
            'type': 'Integer',
            'req': True,
            'default': 1},
        'bmalt': {
            'desc': 'if true => flip sign of alternate particles when BGEN = true.',
            'doc': '',
            'type': 'Logical',
            'req': False,
            'default': False}}

    def __init__(self, **kwargs):
        ICoolObject.__init__(self, kwargs)
        Container.__init__(self)

    def __setattr__(self, name, value):
        Container.__setattr__(self, name, value)