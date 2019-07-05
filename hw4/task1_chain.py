class Someobjcect:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, type_):
        self.type_ = type_


class EventSet:
    def __init__(self, value_):
        self.value_ = value_


class NullHandler:
    def __init__(self, successor=None):
        self. __successor = successor

    def handle(self, objc, event):
        if self. __successor is not None:
            return self. __successor.handle(objc, event)


class IntHandler(NullHandler):
    def handle(self, objc, event):
        if isinstance(event, EventGet):
            if event.type_ is int:
                return objc.integer_field
            else:
                return super().handle(objc, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, int):
                objc.integer_field = event.value_
            else:
                super().handle(objc, event)


class FloatHandler(NullHandler):
    def handle(self, objc, event):
        if isinstance(event, EventGet):
            if event.type_ is float:
                return objc.float_field
            else:
                return super().handle(objc, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, float):
                objc.float_field = event.value_
            else:
                super().handle(objc, event)


class StrHandler(NullHandler):
    def handle(self, objc, event):
        if isinstance(event, EventGet):
            if event.type_ is str:
                return objc.string_field
            else:
                return super().handle(objc, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, str):
                objc.string_field = event.value_
            else:
                super().handle(objc, event)


if __name__ == '__main__':
    objc = Someobjcect()
    objc.integer_field = 42
    objc.float_field = 3.14
    objc.string_field = 'some text'

    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(objc, EventGet(int)))
    print(chain.handle(objc, EventGet(float)))
    print(chain.handle(objc, EventGet(str)))
    chain.handle(objc, EventSet(100))
    print(chain.handle(objc, EventGet(int)))
    chain.handle(objc, EventSet(0.5))
    print(chain.handle(objc, EventGet(float)))
    chain.handle(objc, EventSet('new text'))
    print(chain.handle(objc, EventGet(str)))
