from icoolobject import ICoolObject

class Title(ICoolObject):
    command_params = {
        'title': {'desc': 'Title of ICOOL simulation',
                  'doc': '',
                  'type': 'String',
                  'req': True,
                  'default': None}

    }

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return 'Problem Title: ' + self.title + '\n'

    def __repr__(self):
        return 'Problem Title: ' + self.title + '\n'

    def gen_for001(self, file):
        file.write(self.title)
        file.write('\n')