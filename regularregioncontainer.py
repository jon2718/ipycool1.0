from regularregion import *
from container import *


class RegularRegionContainer(RegularRegion, Container):

    def __init__(self, **kwargs):
        pass
        
    def gen_for001(self, file, command_params_dict):
        Region.gen_for001(self, file, command_params_dict)
        Container.gen_for001(self, file)
        if hasattr(self, 'endtag'):
            file.write(self.get_endtag())
            file.write('\n')