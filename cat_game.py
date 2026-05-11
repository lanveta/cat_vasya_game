import math
from abc import ABC, abstractmethod


class Unit(ABC):
    """Абстрактный класс Юнит"""
    
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass


class Character(Unit):
    """Дочерний класс от Юнит - персонаж"""
    
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        """Возвращает максимальное здоровье персонажа"""
        return math.floor(self.constitution * 10 + self.strength / 2)
    
    def calculate_damage(self):
        """Возвращает урон персонажа"""
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)
    
    def calculate_defense(self):
        """Возвращает защиту персонажа"""
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)


class Monster(Unit):
    """Дочерний класс от Юнит - монстр"""

    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        """Возвращает максимальное здоровье монстра"""
        return math.floor((self.constitution * 8) + (self.strength / 3))
    
    def calculate_damage(self):
        """Возвращает урон монстра"""
        return math.floor((self.strength * 2) + (self.constitution / 5))
    
    def calculate_defense(self):
        """Возвращает защиту монстра"""
        return math.floor((self.constitution * 1.2) + (self.strength / 5))