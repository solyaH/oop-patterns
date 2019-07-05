class SomeObject:
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

    def handle(self, obj, event):
        if self. __successor is not None:
            return self. __successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type_ is int:
                return obj.integer_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, int):
                obj.integer_field = event.value_
            else:
                return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type_ is float:
                return obj.float_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, float):
                obj.float_field = event.value_
            else:
                return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if isinstance(event, EventGet):
            if event.type_ is str:
                return obj.string_field
            else:
                return super().handle(obj, event)
        elif isinstance(event, EventSet):
            if isinstance(event.value_, str):
                obj.string_field = event.value_
            else:
                return super().handle(obj, event)


if __name__ == '__main__':
    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = 'some text'

    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))
    print(chain.handle(obj, EventSet(100)))
    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventSet(0.5)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventSet('new text')))
    print(chain.handle(obj, EventGet(str)))
