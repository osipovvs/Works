class TagException(Exception):
    pass

class Tag(object):
    __slots__ = ('_name', '_attrs', '_parent', '_previous_sibling', '_next_sibling')

    def __init__(self, name, attrs={}):
        self._name = str(name)
        self._attrs = None
        self._parent = None
        self._previous_sibling = None
        self._next_sibling = None
        self.__set_attrs(attrs)

    def __getattribute__(self, attr):
        try:
            return super().__getattribute__(attr)
        except AttributeError:
            return self._attrs.get(attr)

    def __setattr__(self, attr, value):
        try:
            return super().__setattr__(attr, value)
        except AttributeError:
             self._attrs[attr] = value

    def __delattr__(self, attr):
        try:
            super().__delattr__(attr)
        except AttributeError:
            del self._attrs[attr]


    def __set_attrs(self, attrs):
        if not isinstance(attrs, dict):
            raise ValueError
        self._attrs = attrs
            
    @property
    def parent(self):
        '''return self._parent'''
        return self._parent
    
    @parent.setter
    def parent(self, value):
        if not isinstance(value, ContainerTag):
            raise TagException('Tag {} is not a ContainerTag'.format(value))
        self._parent = value

    @parent.deleter
    def parent(self):
        self._parent = None

    @property
    def previous_sibling(self):
        return self._previous_sibling
    
    @previous_sibling.setter
    def previous_sibling(self, value):
        self._previous_sibling = value

    @previous_sibling.deleter
    def previous_sibling(self):
        self._previous_sibling = None


    @property
    def next_sibling(self):
        return self._next_sibling
    
    @next_sibling.setter
    def next_sibling(self, value):
        self._next_sibling = value

    @next_sibling.deleter
    def next_sibling(self):
        self._next_sibling = None

    @property
    def children(self):
        raise TagException('Not a container tag!')

    @property
    def first_child(self):
        raise TagException('Not a container tag!')

    @property
    def last_child(self):
        raise TagException('Not a container tag!')


class ContainerTag(Tag):
    pass




if __name__ == '__main__':

    a = Tag('a')
    a.href = 'www.python.org'
    a.klass = 'active'
    print(a.href)

    img = Tag('img')
    img.src = '/python-developer.svg'
    img.alt = 'Python Разработчик'
    print(img)