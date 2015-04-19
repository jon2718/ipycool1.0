from icoolobject import *


class Container(ICoolObject):

    """Abstract class container for other commands.
    """

    command_params = {
        'enclosed_commands': {
            'desc': 'Commands enclosed in this container',
            'doc': '',
            'type': 'Array',
            'req': False}
           
    }

    def __init__(self, **kwargs):
        ICoolObject.check_command_params_init(self, Container.command_params, **kwargs)

    def __setattr__(self, name, value):
        self.__icool_setattr__(name, value, Container.command_params)

    def __str__(self):
        ret_str = ''
        for command in self.enclosed_commands:
            ret_str += str(command)
        return ret_str

    def add_enclosed_command(self, command):
        if self.check_allowed_enclosed_command(command) is False:
            sys.exit(0)
        else:
            if not hasattr(self, 'enclosed_commands'):
                self.enclosed_commands = []
            self.enclosed_commands.append(command)

    def insert_enclosed_command(self, command, insert_point):
        if self.check_allowed_command(command) is False:
            sys.exit(0)
        else:
            self.enclosed_commands.insert(insert_point, command)

    def remove_enclosed_command(self, delete_point):
        del self.enclosed_commands[delete_point]

    def check_allowed_enclosed_command(self, command):
        try:
            if command.__class__.__name__ not in self.allowed_enclosed_commands:
                raise ie.ContainerCommandError(
                    command,
                    self.allowed_enclosed_commands)
        except ie.ContainerCommandError as e:
            print e
            return False
        return True

    def check_allowed_enclosed_commands(self, enclosed_commands):
        pass

    def gen_for001(self, file):
        for command in self.enclosed_commands:
            print 'Command is: ', command
            if hasattr(command, 'gen_for001'):
                command.gen_for001(file)
            else:
                file.write(self.for001_str_gen(command))
