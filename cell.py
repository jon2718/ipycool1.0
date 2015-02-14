from regularregioncontainer import *


class Cell(RegularRegionContainer):

    """CELL Start of a repeating group of region commands; the data must end with an ENDCELL command.
    The cell loop can enclose any number of commands under REPEAT plus REPEAT and ENDREPEAT commands.
    It has an associated cell field, which is superimposed on the individual region fields. Cell sections cannot
    be nested in other cell sections. (see parameters below)
    """
    begtag = 'CELL'
    endtag = 'ENDCELL'
    num_params = 3
    for001_format = {'line_splits': [1, 1, 1]}

    allowed_enclosed_commands = [
        'SRegion',
        'Aperture',
        'Dens',
        'Disp',
        'Dummy',
        'DVar',
        'Edge',
        'Output',
        'Refp',
        'Ref2',
        'Reset',
        'RKick',
        'Rotate',
        'Tilt',
        'Transport',
        'Repeat']

    command_params = {
        'ncells': {
            'desc': 'Number of times to repeat this command in this cell block',
            'doc': '',
            'type': 'Integer',
            'req': True,
            'pos': 1},
        'flip': {
            'desc': 'if .true. => flip cell field for alternate cells',
            'doc': '',
            'type': 'Logical',
            'req': True,
            'pos': 2},
        'field': {
            'desc': 'Field object',
            'doc': '',
            'type': 'Field',
            'req': True,
            'pos': 3},
    }

    def __init__(self, **kwargs):
        RegularRegion.__init__(self, kwargs)
        Container.__init__(self)

    def __setattr__(self, name, value):
        Container.__setattr__(self, name, value)

    def __str__(self):
        return_str = 'CELL\n' + str(Container.__str__(self)) + 'ENDCELL\n'
        # for command in self.enclosed_commands:
        #    return_str += str(command)
        return return_str

    def __repr__(self):
        return 'Cell\n'