from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubcribe(self, subscriber):
        pass

    @abstractmethod
    def notify(self, message):
        pass


class ObservableEngine(Engine):
    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        self.__subscribers.add(
            subscriber)

    def unsubcribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def notify(self, message):
        for subscriber in self.__subscribers:
            if subscriber.name == message['title']:
                subscriber.update(message['text'])


class AbstractObserver(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter (AbstractObserver):
    def __init__(self, name):
        super().__init__(name)
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message)


class FullNotificationPrinter (AbstractObserver):
    def __init__(self, name):
        super().__init__(name)
        self.achievements = []

    def update(self, message):
        self.achievements.append(message)


if __name__ == '__main__':
    engine = ObservableEngine()
    full_subs1 = ShortNotificationPrinter('Subs1')
    short_subs1 = FullNotificationPrinter('Subs1')
    full_subs2 = FullNotificationPrinter('Subs2')
    engine.subscribe(full_subs1)
    engine.subscribe(short_subs1)
    engine.subscribe(full_subs2)

    message1 = {'title': 'Subs1', 'text': 'New achievement'}
    message2 = {'title': 'Subs1', 'text': 'New achievement'}
    message3 = {'title': 'Subs1', 'text': 'All levels completed'}
    message4 = {'title': 'Subs2', 'text': 'Other new achievement'}
    engine.notify(message1)
    engine.notify(message2)
    engine.notify(message3)
    engine.notify(message4)
    # engine.notify('All levels completed')
    print('Subs1 : {}'.format(full_subs1.achievements))
    print('Subs1 : {}'.format(short_subs1.achievements))
    print('Subs2 : {}'.format(full_subs2.achievements))
