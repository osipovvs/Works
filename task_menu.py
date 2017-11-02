from abc import ABCMeta, abstractmethod

from collections import namedtuple

class CommandException(Exception):
    pass


class Command(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @abstractmethod
    def execute(self):
        pass


class Menu(object):
    cmds = {}
    counter = -1 
    
    def __iter__(self):
        return self

    def __next__(self):
        # names = list(self.cmds.keys())
        # klasses = list(self.cmds.values())
        items = list(self.cmds.items())
        if self.counter < len(self.cmds) - 1:
            self.counter += 1
            return items[self.counter]
        else:
            raise StopIteration

    # def show_attrs(self):
    #     return self.names, self.klasses


    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

        cls.cmds[name] = klass


    def execute(self, name, *args, **kwargs):
        if not self.cmds.get(name):
            raise CommandException('Command with name "{}" not found'.format(name))

        print('''Command "{}" is to be executed
            with following argument(s): {}'''.format(name, args))




class ListCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass


class ShowCommand(Command):
    def __init__(self, task_id):
       pass

    def execute(self):
        pass



if __name__ == '__main__':

    menu = Menu()
    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    

    # menu.execute('list')
    # menu.execute('show', 5)

    # for i in menu:
    #     print(i)

    for name, command in menu:
        print(name, command)

    # print(Menu.cmds)
    menu.execute('list')
    #print(menu.show_attrs())





