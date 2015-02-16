from modeledcommandparameter import ModeledCommandParameter

class Field(ModeledCommandParameter):

    """
    A Field is a:
    FTAG - A tag identifying the field.  Valid FTAGS are:
    NONE, ACCEL, BLOCK, BROD, BSOL, COIL, DIP, EFLD, FOFO, HDIP, HELI(
        X), HORN, KICK, QUAD,
    ROD, SEX, SHEE(T), SOL, SQUA, STUS, WIG

    FPARM - 15 parameters describing the field.  The first parameter is the model.
    """

    def __init__(self, ftag, kwargs):
        ModeledCommandParameter.__init__(self, kwargs)
        self.ftag = ftag

    def __call__(self, kwargs):
        ModeledCommandParameter.__call__(self, kwargs)

    def __setattr__(self, name, value):
        if name == 'fparm':
            object.__setattr__(self, name, value)
        else:
            ModeledCommandParameter.__setattr__(self, name, value)

    def __str__(self):
        return self.ftag + ':' + 'Field:' + \
            ModeledCommandParameter.__str__(self)

    def gen_fparm(self):
        self.fparm = [0] * 10
        cur_model = self.get_model_dict(self.model)
        for key in cur_model:
            pos = int(cur_model[key]['pos']) - 1
            if key == self.get_model_descriptor_name():
                val = self.get_icool_model_name()
            else:
                val = getattr(self, key)
            self.fparm[pos] = val
        print self.fparm
