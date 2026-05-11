"""
Файл, содержащий 3 класса и описания их структуры:  
Unit (ABC) - абстрактный класс, содержащий все характеристики и абстрактные методы;
Character - наследующий класс от Unit реализующий calculate_max_health, calculate_damage и calculate_defense 
с помощью проверки атрибута character_class;
Spell (ABC) - абстрактный класс с названием, уроном и стоимостью маны, и хотя бы три конкретных заклинания.
"""

import math
from abc import ABC, abstractmethod

class Unit(ABC):
    """Абстрактный класс Юнит"""

    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int) -> None:
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self) -> int:
        pass

    @abstractmethod
    def calculate_damage(self) -> int:
        pass

    @abstractmethod
    def calculate_defense(self) -> int:
        pass

    def add_spell(self, spell: "Spell") -> None:
        """Добавляет заклинание в список доступных"""

        if isinstance(spell, Spell):
            self.spells.append(spell)
        else:
            raise TypeError("Можно добавить только объект класса Spell")

    def cast_spell(self, index: int) -> int:
        """Применяет заклинание по индексу, если хватает маны"""

        if index < 0 or index >= len(self.spells):
            raise IndexError("Неверный индекс заклинания")
        spell = self.spells[index]
        if self.mana < spell.mana_cost:
            raise ValueError(f"Недостаточно маны! Нужно {spell.mana_cost}, есть {self.mana}")
        self.mana -= spell.mana_cost
        return spell.cast()


class Spell (ABC):
    """Абстрактный класс заклинания"""

    def __init__(self, name: str, damage: int, mana_cost: int) -> None:
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self) -> int:
        pass

class Fireball(Spell):
    """Дочерний класс от Spell с заклинанием огненный шар"""
    
    def __init__(self) -> None:
        super().__init__('Fireball', 35, 15)
    
    def cast(self) -> int:
        return self.damage

class IceLance(Spell):
    """Дочерний класс от Spell с заклинанием ледяное копьё"""
    
    def __init__(self) -> None:
        super().__init__('IceLance', 25, 10)
    
    def cast(self) -> int:
        return self.damage

class LightningBolt(Spell):
    """Дочерний класс от Spell с заклинанием молния"""
    
    def __init__(self) -> None:
        super().__init__('LightningBolt', 40, 20)
    
    def cast(self) -> int:
        return self.damage
    

class Character(Unit):
    """Дочерний класс от Юнит - персонаж"""

    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int, character_class: str) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        self.character_class = character_class

        self.max_health = self.calculate_max_health()
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()
        self.max_mana = self.calculate_max_mana()
        self.mana = self.max_mana

    def calculate_max_health(self) -> int:
        """Возвращает максимальное здоровье персонажа"""
        return math.floor(self.constitution * 10 + self.strength / 2)
    
    def calculate_damage(self) -> int:
        """Возвращает урон персонажа"""
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)
    
    def calculate_defense(self) -> int:
        """Возвращает защиту персонажа"""
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)
        
    def calculate_max_mana(self) -> int:
        """Возвращает максимальную ману персонажа"""
        
        if self.character_class == 'warrior':
            return math.floor(self.intelligence + self.strength / 2)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 3 + self.wisdom)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.5 + self.wisdom / 2)
        

class Monster(Unit):
    """Дочерний класс от Юнит - монстр"""

    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int) -> None:
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self) -> int:
        """Возвращает максимальное здоровье монстра"""
        return math.floor((self.constitution * 8) + (self.strength / 3))
    
    def calculate_damage(self) -> int:
        """Возвращает урон монстра"""
        return math.floor((self.strength * 2) + (self.constitution / 5))
    
    def calculate_defense(self) -> int:
        """Возвращает защиту монстра"""
        return math.floor((self.constitution * 1.2) + (self.strength / 5))
