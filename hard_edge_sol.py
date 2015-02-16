from sol import Sol
from material import Material
from subregion import SubRegion
from sregion import SRegion
from region import Region

class HardEdgeSol(Region):
    """
    Hard edge solenoid comprises:
    (1) Entrance focusing region;
    (2) Non-focusing constant solenoid region;
    (3) Exit focusing region
    """
    begtag = ''
    endtag = ''
    num_params = 1

    command_params = {
        'mtag': {'desc': 'Material tag',
                 'doc': '',
                 'type': 'String',
                 'req': True,
                 'pos': None},
        'geom': {'desc': 'Geometry',
                 'doc': '',
                 'type': 'String',
                 'req': True,
                 'pos': None},
        'bs':   {'desc': 'Field strength (Tesla)',
                 'doc': '',
                 'type': 'Float',
                 'req': True,
                 'pos': None},
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

        'sreg_entrance': {'desc': 'Entrance SRegion',
                          'doc': '',
                          'type': 'SRegion',
                          'req': False,
                          'pos': None},
        'sreg_exit':     {'desc': 'Exit SRegion',
                          'doc': '',
                          'type': 'SRegion',
                          'req': False,
                          'pos': None},
        'sreg_body': {'desc': 'Body SRegion',
                              'doc': '',
                              'type': 'SRegion',
                              'req': False,
                              'pos': None}

    }
    
    def __init__(self, **kwargs):
        Region.__init__(self, kwargs)
        material = Material(geom=self.geom, mtag=self.mtag)
        
        # Entrance SRegion
        sol_ent = Sol(model='edge', ent_def=0, ex_def=0, foc_flag=2, bs=self.bs)
        ent_subregion = SubRegion(material=material, rlow=0, rhigh=self.rhigh, irreg=1, field=sol_ent)
        self.sreg_entrance = SRegion(zstep=self.zstep, nrreg=1, slen=0)
        self.sreg_entrance.add_enclosed_command(ent_subregion)

        # Exit SRegion
        sol_exit = Sol(model='edge', ent_def=0, ex_def=0, foc_flag=1, bs=self.bs)
        exit_subregion = SubRegion(material=material, rlow=0, rhigh=self.rhigh, irreg=1, field=sol_exit)
        self.sreg_exit = SRegion(zstep=self.zstep, nrreg=1, slen=0)
        self.sreg_exit.add_enclosed_command(exit_subregion)

        # Body SRegion
        sol_body = Sol(model='edge', ent_def=0, ex_def=0, foc_flag=0, bs=self.bs)
        body_subregion = SubRegion(material=material, rlow=0, rhigh=self.rhigh, irreg=1, field=sol_body)
        self.sreg_body = SRegion(zstep=self.zstep, nrreg=1, slen=self.slen)
        self.sreg_body.add_enclosed_command(body_subregion)

    def __call__(self, **kwargs):
        Region.__call__(self, kwargs)

    def gen_for001(self, file):
        self.sreg_entrance.gen_for001(self, file)
        self.sreg_body.gen_for001(self, file)
        self.sreg_exit.gen_for001(self, file)

