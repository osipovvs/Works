from abc import ABCMeta, abstractmethod
from datetime import datetime

class ValidatorException(Exception):
    pass


class Validator(metaclass=ABCMeta):
    # def __init__(self, value):
    #     self.value = value

    @abstractmethod
    def validate(self):
        pass

    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ValidatorException("Validator must have a name!")

        if not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))

        cls.types[name] = klass


    @classmethod
    def get_instance(cls, name):
        klass = cls.types.get(name)
        
        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))

        return klass()


class EMailValidator(Validator):
    def validate(self, value):
        self.value = value
        if not '@' in value:
            return False

        for char in value:
            if char in ' ,:;<>[]/\\':
                return False
        
        parts = value.split('@')
        
        if len(parts) != 2:
            return False
        if len(parts[0]) > 63 or len(parts[1]) > 63:
            return False

        domain_parts = parts[1].split('.')
        
        if not domain_parts[-1].isalpha() or not domain_parts[-1].islower():
            return False

        return True
        

class DateTimeValidator(Validator):

    def validate(self, value):
        dt_formats = {
        '--': '%Y-%m-%d',
        '..': '%d.%m.%Y',
        '//': '%d/%m/%Y',
        '-- :': '%Y-%m-%d %H:%M',
        '.. :': '%d.%m.%Y %H:%M',
        '// :': '%d/%m/%Y %H:%M',
        '-- ::': '%Y-%m-%d %H:%M:%S',
        '.. ::': '%d.%m.%Y %H:%M:%S',
        '// ::': '%d/%m/%Y %H:%M:%S'
        }

        key = value

        for i in value:
            if i.isdigit():
                key = key.replace(i, '')

        try:
            datetime.strptime(value, str(dt_formats.get(key)))
        except ValueError: return False
        else: return True


    

if __name__ == '__main__':

    Validator.add_type('email', EMailValidator)
    Validator.add_type('datetime', DateTimeValidator)

    validator = Validator.get_instance('email')
    print(validator.validate('somet[hing@mail.ru'))

    print(Validator.types)

    validator = Validator.get_instance('datetime')
    print(validator.validate('1.9.2017'))

