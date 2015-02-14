from region import *


class RegularRegion(Region):

    """
    RegularRegion commands include: SECTION, BEGS, REPEAT, CELL, SREGION, ENDREPEAT, ENDCELL,
    and ENDCELL.
    """

    def __init__(self, kwargs):
        Region.__init__(self, kwargs)

    def __str__(self):
        return '[A RegularRegion can be either a SECTION, BEGS, REPEAT, CELL, SREGION, ENDREPEAT, ENDCELL,\
or ENDCELL.]'

    def __repr__(self):
        return '[A RegularRegion can be either a SECTION, BEGS, REPEAT, CELL, SREGION, ENDREPEAT, ENDCELL,\
                or ENDCELL.]'