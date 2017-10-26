from abc import ABCMeta, abstractmethod
import os

class ParamHandlerException(Exception):
    pass

class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_all_params(self):
        return self.params

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @staticmethod
    def get_instance(source):
        _, ext = os.path.splitext(str(source).lower())

        if ext == '.json':
            return JsonParamHandler(source)

        if ext == '.pickle':
            return PickleParamHandler(source)

        return TextParamHandler(source)

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException("Type must have a name!")

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not a ParamHandler!'.format(klass)
            )

        cls.types[name] = klass

    @classmethod
    def get_instance(cls, source, *args, **kwargs):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)

        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found!'.format(ext)
            )

        return klass(source, *args, **kwargs)

class TextParamHandler(ParamHandler):
    def read(self):
        with open(self.source, 'r') as f:
            self.params = f.read()

    def write(self):
        with open(self.source, 'w') as f:
            f.write(self.params)


class PickleParamHandler(ParamHandler):
    def read(self):
        import pickle
        with open(self.source, 'rb') as f:
            self.params = pickle.load(f)

    def write(self):
        import pickle
        with open(self.source, 'wb') as f:
            pickle.dump(self.params, f)


class JsonParamHandler(ParamHandler):
    def read(self):
        pass

    def write(self):
        pass

ParamHandler.add_type('pickle', PickleParamHandler)

config = ParamHandler.get_instance('./parameters.pickle')
#config.add_param('key1', 'value1')
#config.write()

config.read()

print(config.get_all_params())