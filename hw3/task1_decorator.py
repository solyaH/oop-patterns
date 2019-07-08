class NullHandler:
    def __init__(self, successor=None):
        self. __successor = successor

    def handle(self, objc, event):
        if self. __successor is not None:
            self. __successor.handle(objc, event)


class BerserkHandler(NullHandler):
    def handle(self, objc, cls):
        if cls is Berserk:
            if 'Berserk' in objc.get_positive_effects():
                objc.stats['HP'] -= 50
                objc.stats['Strength'] += 7
                objc.stats['Endurance'] += 7
                objc.stats['Agility'] += 7
                objc.stats['Luck'] += 7
                objc.stats['Perception'] += 3
                objc.stats['Charisma'] += 3
                objc.stats['Intelligence'] += 3
                objc.positive_effects.remove('Berserk')
        else:
            super().handle(objc, cls)


class BlessingHandler(NullHandler):
    def handle(self, objc, cls):
        if cls is Blessing:
            if 'Blessing' in objc.get_positive_effects():
                objc.stats['Strength'] -= 2
                objc.stats['Endurance'] -= 2
                objc.stats['Agility'] -= 2
                objc.stats['Luck'] -= 2
                objc.stats['Perception'] -= 2
                objc.stats['Charisma'] -= 2
                objc.stats['Intelligence'] -= 2
                objc.positive_effects.remove('Blessing')
        else:
            super().handle(objc, cls)


class WeaknessHandler(NullHandler):
    def handle(self, objc, cls):
        if cls is Curse:
            if 'Weakness' in objc.get_negative_effects():
                objc.stats['Strength'] += 4
                objc.stats['Endurance'] += 4
                objc.stats['Agility'] += 4
                objc.negative_effects.remove('Weakness')
        else:
            super().handle(objc, cls)


class EvilEyeHandler(NullHandler):
    def handle(self, objc, cls):
        if cls is EvilEye:
            if 'EvilEye' in objc.get_negative_effects():
                objc.stats['Luck'] += 10
                objc.negative_effects.remove('EvilEye')
        else:
            super().handle(objc, cls)


class CurseHandler(NullHandler):
    def handle(self, objc, cls):
        if cls is Curse:
            if 'Curse' in objc.get_negative_effects():
                objc.stats['Strength'] += 2
                objc.stats['Endurance'] += 2
                objc.stats['Agility'] += 2
                objc.stats['Luck'] += 2
                objc.stats['Perception'] += 2
                objc.stats['Charisma'] += 2
                objc.stats['Intelligence'] += 2
                objc.negative_effects.remove('Curse')
        else:
            super().handle(objc, cls)


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

    def remove_effect(self, cls):
        chain = EvilEyeHandler(WeaknessHandler(
            CurseHandler(BlessingHandler(BerserkHandler(NullHandler)))))
        chain.handle(self, cls)


class AbstractEffect(Hero):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj
        self.positive_effects = self.obj.get_positive_effects()
        self.negative_effects = self.obj.get_negative_effects()
        self.stats = self.obj.get_stats()


class AbstractPositive(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)


class AbstractNegative(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        obj_stats = self.obj.get_stats()
        self.stats['HP'] = obj_stats['HP'] + 50
        self.stats['Strength'] = obj_stats['Strength'] - 7
        self.stats['Endurance'] = obj_stats['Endurance'] - 7
        self.stats['Agility'] = obj_stats['Agility'] - 7
        self.stats['Luck'] = obj_stats['Luck'] - 7
        self.stats['Perception'] = obj_stats['Perception'] - 3
        self.stats['Charisma'] = obj_stats['Charisma'] - 3
        self.stats['Intelligence'] = obj_stats['Intelligence'] - 3
        self.positive_effects.append('Berserk')


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        obj_stats = self.obj.get_stats()
        self.stats['Strength'] = obj_stats['Strength'] + 2
        self.stats['Endurance'] = obj_stats['Endurance'] + 2
        self.stats['Agility'] = obj_stats['Agility'] + 2
        self.stats['Luck'] = obj_stats['Luck'] + 2
        self.stats['Perception'] = obj_stats['Perception'] + 2
        self.stats['Charisma'] = obj_stats['Charisma'] + 2
        self.stats['Intelligence'] = obj_stats['Intelligence'] + 2
        # self.positive_effects = self.obj.get_positive_effects()
        self.positive_effects.append('Blessing')


class Weakness(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        obj_stats = self.obj.get_stats()
        self.stats['Strength'] = obj_stats['Strength'] - 4
        self.stats['Endurance'] = obj_stats['Endurance'] - 4
        self.stats['Agility'] = obj_stats['Agility'] - 4
        # self.negative_effects = self.obj.get_negative_effects()
        self.negative_effects.append('Weakness')


class EvilEye(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        obj_stats = self.obj.get_stats()
        self.stats['Luck'] = obj_stats['Luck'] - 10
        self.negative_effects.append('EvilEye')


class Curse(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        obj_stats = self.obj.get_stats()
        self.stats['Strength'] = obj_stats['Strength'] - 2
        self.stats['Endurance'] = obj_stats['Endurance'] - 2
        self.stats['Agility'] = obj_stats['Agility'] - 2
        self.stats['Luck'] = obj_stats['Luck'] - 2
        self.stats['Perception'] = obj_stats['Perception'] - 2
        self.stats['Charisma'] = obj_stats['Charisma'] - 2
        self.stats['Intelligence'] = obj_stats['Intelligence'] - 2
        # self.positive_effects = self.obj.get_positive_effects()
        self.negative_effects.append('Curse')


if __name__ == '__main__':
    hero = Hero()
    # print(hero.get_stats())
    # print(hero.get_negative_effects())
    # print(hero.get_positive_effects())

    brs1 = Berserk(hero)
    # print(brs1.get_stats())
    # print(brs1.get_negative_effects())
    # print(brs1.get_positive_effects())

    brs2 = Berserk(brs1)

    cur1 = Curse(brs2)
    print(cur1.get_stats())
    print(cur1.get_negative_effects())
    print(cur1.get_positive_effects())

    cur1.remove_effect(Berserk)
    print(cur1.get_stats())
    print(cur1.get_negative_effects())
    print(cur1.get_positive_effects())
