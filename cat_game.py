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

    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
         super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        """Возвращает максимальное здоровье персонажа"""
        return math.floor((self.constitution * 10) + (self.strength / 2)) 
    
    def calculate_damage(self):
        """Возвращает урон песронажа"""
        return math.floor((self.strength * 1.5) + (self.dexterity / 4))

    def calculate_defense(self):
        """Возвращает защиту персонажа"""
        return math.floor((self.constitution * 1.5) + (self.dexterity / 3))

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