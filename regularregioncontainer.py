from regularregion import *
from container import *


class RegularRegionContainer(RegularRegion, Container):

    def __init__(self, **kwargs):
        if 'enclosed_commands' in kwargs.keys():
            Container.__init__(self, kwargs['enclosed_commands'])
        else:
            Container.__init__(self)
        RegularRegion.__init__(self, **kwargs)
        

    def gen_for001(self, file):
        Region.gen_for001(self, file)
        Container.gen_for001(self, file)
        if hasattr(self, 'endtag'):
            file.write(self.get_endtag())
            file.write('\n')