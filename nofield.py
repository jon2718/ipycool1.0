from field import *


class NoField(Field):

    """No Field"""
    begtag = 'NONE'
    endtag = ''

    models = {
        'model_descriptor': {'desc': 'Name of model parameter descriptor',
                                     'name': None,
                                     'num_parms': 15,
                                     'for001_format': {'line_splits': [15]}},
    }

    def __init__(self, **kwargs):
        Field.__init__(self, 'NONE', kwargs)

    def __call__(self, **kwargs):
        Field.__call__(self, kwargs)

    def __setattr__(self, name, value):
        if name == 'ftag':
            if value == 'NONE':
                object.__setattr__(self, name, value)
            else:
                # Should raise exception here
                print '\n Illegal attempt to set incorrect ftag.\n'
        else:
            Field.__setattr__(self, name, value)

    def __str__(self):
        # return Field.__str__(self)
        return 'NONE'

    def gen_fparm(self):
        Field.gen_fparm(self)