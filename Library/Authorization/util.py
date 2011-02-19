import sys
__version__ = '0.3'
class WrappedInt(int):
    def __new__(klass, v=0):
        if isinstance(v, long) and not (-sys.maxint <= v <= sys.maxint):
            if not (sys.maxint < v <= 0xFFFFFFFFL):
                raise ValueError, 'Can not wrap'
            return int.__new__(klass, v - 0x100000000L)
        return int.__new__(klass, v)
            
class MetaEnumerator(type):
    def __new__(klass, name, bases, dct):
        # use a wrapped integer as the default metatype
        basetype = dct.get('__basetype__', WrappedInt)

        class enumvalue(basetype):
            __name__ = name + '_value'
            def __new__(klass, name, value, doc=None):
                #print '%r, %r, %r' % (klass, name, value)
                self = basetype.__new__(klass, value)
                self.name = name
                self.value = value
                self.doc = doc
                return self

            def __str__(self):
                return self.name

            def __repr__(self):
                if self.doc is None:
                    return '%s.%s(%s)' % (
                        self.enumerator.__name__,
                        self.name,
                        self.__class__.__bases__[0].__repr__(self),
                    )
                else:
                    return '%s.%s(%s, %r)' % (
                        self.enumerator.__name__,
                        self.name,
                        self.__class__.__bases__[0].__repr__(self),
                        self.doc,
                    )

        #print '%r, %r, %r, %r' % (klass, name, bases, dct,)
        values = {}
        keys = {}
        for k, v in dct.items():
            if k.startswith('_') or k.endswith('__doc__'):
                continue
            docattr = k+'__doc__'
            if docattr in dct:
                doc = dct[docattr]
                del dct[docattr]
            else:
                doc = None
            v = enumvalue(k, v, doc)
            values[v] = k
            dct[k] = keys[k] = v
        dct['__keys__'] = keys
        dct['__values__'] = values
        dct['__basetype__'] = enumvalue
        enumtype = type.__new__(klass, name, bases, dct)
        enumvalue.enumerator = enumtype
        return enumtype

    def fromValue(self, value):
        return self.__keys__[self.__values__[value]]

    def fromName(self, name):
        return self.__keys__[name]

    def fromFlags(self, value):
        return [v for v in self.__values__ if ((value & v) == v)]

    def __contains__(self, value):
        return value in self.__values__

    def __getitem__(self, value):
        return self.__values__[value]

class Enumerator:
    __metaclass__ = MetaEnumerator
