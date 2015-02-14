from regularregion import *
from container import *


class RegularRegionContainer(RegularRegion, Container):

    def gen_for001(self, file):
        # self.gen_begtag(file)
        # if hasattr(self, 'begtag'):
        #    print 'Writing begtag'
        #    file.write(self.get_begtag())
        #    file.write('\n')
        Region.gen_for001(self, file)
        Container.gen_for001(self, file)
        # self.gen_endtag(file)
        if hasattr(self, 'endtag'):
            file.write(self.get_endtag())
            file.write('\n')