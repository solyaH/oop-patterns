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


class AbstractEffect(Hero):
    def __init__(self, obj):
        # super().__init__()
        self.obj = obj

    def get_positive_effects(self):
        return self.obj.get_positive_effects()

    def get_negative_effects(self):
        return self.obj.get_negative_effects()

    def get_stats(self):
        return self.obj.get_stats()


class AbstractPositive(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)


class AbstractNegative(AbstractEffect):
    def __init__(self, obj):
        super().__init__(obj)


class Berserk(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        self.obj.stats['HP'] += 50
        self.obj.stats['Strength'] += 7
        self.obj.stats['Endurance'] += 7
        self.obj.stats['Agility'] += 7
        self.obj.stats['Luck'] += 7
        self.obj.stats['Perception'] -= 3
        self.obj.stats['Charisma'] -= 3
        self.obj.stats['Intelligence'] -= 3
        self.obj.positive_effects.append('Berserk')


class Blessing(AbstractPositive):
    def __init__(self, obj):
        super().__init__(obj)
        self.obj.stats['Strength'] += 2
        self.obj.stats['Endurance'] += 2
        self.obj.stats['Agility'] += 2
        self.obj.stats['Luck'] += 2
        self.obj.stats['Perception'] += 2
        self.obj.stats['Charisma'] += 2
        self.obj.stats['Intelligence'] += 2
        self.obj.positive_effects.append('Blessing')


class Weakness(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        self.obj.stats['Strength'] -= 4
        self.obj.stats['Endurance'] -= 4
        self.obj.stats['Agility'] -= 4
        self.obj.negative_effects.append('Weakness')


class EvilEye(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        self.obj.stats['Luck'] -= 10
        self.obj.negative_effects.append('EvilEye')


class Curse(AbstractNegative):
    def __init__(self, obj):
        super().__init__(obj)
        self.obj.stats['Strength'] -= 2
        self.obj.stats['Endurance'] -= 2
        self.obj.stats['Agility'] -= 2
        self.obj.stats['Luck'] -= 2
        self.obj.stats['Perception'] -= 2
        self.obj.stats['Charisma'] -= 2
        self.obj.stats['Intelligence'] -= 2
        self.obj.negative_effects.append('Curse')


if __name__ == '__main__':
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_negative_effects())
    print(hero.get_positive_effects())
    brs1 = Berserk(hero)
    print(brs1.get_stats())
    print(brs1.get_negative_effects())
    print(brs1.get_positive_effects())

    # brs2 = Berserk(hero)
    cur1 = Curse(hero)
    print(cur1.get_stats())
    print(cur1.get_negative_effects())
    print(cur1.get_positive_effects())
