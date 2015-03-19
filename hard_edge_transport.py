from sol import Sol
from cell import Cell
from icool_composite import ICoolComposite
from icoolobject import ICoolObject
from cell import *


class HardEdgeTransport(ICoolComposite, Cell):
    """
    Hard edge transport comprises:
    (1) Cell with hard edge solenoid field (SOL model 8)
    """
    begtag = ''
    endtag = ''
    num_params = 1

    command_params = {
        'bs':   {'desc': 'Field strength (Tesla)',
                 'doc': '',
                 'type': 'Float',
                 'req': True,
                 'pos': None},

        'flip':   {'desc': 'Cell flip',
                   'doc': 'If .true. flip cell field for alternate cells',
                   'type': 'Boolean',
                   'req': True,
                   'pos': None},

        'transport_cell': {'desc': 'Transport cell',
                           'doc': '',
                           'type': 'Cell',
                           'req': False,
                           'pos': None}
    }
    
    def __init__(self, **kwargs):
        ICoolObject.__init__(self, kwargs)
        he_sol = Sol(model='edge', ent_def=0, ex_def=0, foc_flag=0, bs=self.bs)
        Cell.__init__(self, ncells=1, flip=False, field=he_sol)
        

    def __call__(self, **kwargs):
        ICoolObject.__call__(self, kwargs)

    def __str__(self):
        return 'HardEdgeTransport'

    def add_enclosed_command(self, command):
        self.transport_cell.add_enclosed_command(command)

    def gen_for001(self, file):
        self.gen_for001(file)
