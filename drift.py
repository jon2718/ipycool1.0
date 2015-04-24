from material import Material
from subregion import SubRegion
from sregion import SRegion
from icool_composite import ICoolComposite
from icoolobject import ICoolObject
from nofield import NoField


class Drift(ICoolObject):
    """
    Drift region.
    By default will generate a vacuum drift region with cylindrical geometry.
    """
    begtag = ''
    endtag = ''
    num_params = 10

    command_params = {
        'slen': {'desc': 'SRegion length',
                 'doc': '',
                 'type': 'Float',
                 'req': True,
                 'pos': None},
        'zstep': {'desc': 'Z step',
                  'doc': '',
                  'type': 'Float',
                  'req': True,
                  'pos': None},
        'rhigh': {'desc': 'R high',
                  'doc': '',
                  'type': 'Float',
                  'req': True,
                  'pos': None},
        'outstep': {'desc': 'Output stepping (Meter)',
                    'doc': 'Increment for output steps for constant B Field region',
                    'type': 'Float',
                    'req': True,
                    'pos': None},
    }

    def __init__(self, **kwargs):
        ICoolObject.__init__(self, kwargs)
        material = Material(geom='CBLOCK', mtag='VAC')
        nf = NoField()
        sr = SubRegion(material=material, rlow=0, rhigh=self.rhigh, irreg=1, field=nf)
        self.sreg = SRegion(zstep=self.zstep, nrreg=1, slen=self.slen)
        self.sreg.add_enclosed_command(sr)

    def __call__(self, **kwargs):
        ICoolObject.__call__(self, kwargs)

    def __str__(self):
        return 'Drift'

    def gen_for001(self, file):
        self.sreg.gen_for001(file)
       
