from regularregioncontainer import *


class Section(RegularRegionContainer):

    """
    SECTION Start of cooling section region definition.
    The data must end with an ENDSECTION.   It can enclose any number of other commands.
    If it is desired to repeat the section definitions, the control variable NSECTIONS should be
    set >1 and a BEGS command is used to define where to start repeating.
    """

    begtag = 'SECTION'
    endtag = 'ENDSECTION'
    num_params = 0
    for001_format = {'line_splits': [0]}

    allowed_enclosed_commands = [
        'Begs',
        'Repeat',
        'Cell',
        'Background',
        'SRegion',
        'Aperture',
        'Cutv',
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
        'Comment',
        'Repeat',
        'HardEdgeSol']

    command_params = {

    }

    def __init__(self, **kwargs):
        RegularRegion.__init__(self, kwargs)
        Container.__init__(self)

    def __setattr__(self, name, value):
        Container.__setattr__(self, name, value)

    def __str__(self):
        return_str = 'SECTION\n'
        return_str += str(Container.__str__(self))
        return_str += 'END_SECTION\n'
        return return_str

    def __repr__(self):
        return 'Section\n'