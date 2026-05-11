## cat_vasya_game

МОДУЛЬ 1

Реализует базовую иерархию классов для игровых сущностей (персонажи и монстры) с единым интерфейсом расчёта боевых характеристик.

Структура:

    Unit (абстрактный класс)
        - Атрибуты: strength, dexterity, constitution, wisdom, intelligence, charisma
        - Абстрактные методы: calculate_max_health(), calculate_damage(), calculate_defense()

    Character (наследуется от Unit) — игровой персонаж
        Формулы:
            health  = floor(constitution × 10 + strength / 2) - максимальное здоровье пероснажа
            damage  = floor(strength × 1.5 + dexterity / 4) - урон персонажа
            defense = floor(constitution × 1.5 + dexterity / 3) - защита персонажа

    Monster (наследуется от Unit) — противник
        Формулы:
            health  = floor(constitution × 8 + strength / 3) - максимальное здоровье монстра
            damage  = floor(strength × 2 + constitution / 5) - урон монстра
            defense = floor(constitution × 1.2 + strength / 5) - защита монстра

Особенности:
- Используется abc.ABC для обеспечения единого интерфейса
- Все расчёты возвращают целые числа (math.floor)
- Необязательные атрибуты инициализируются нулём
- Разные формулы обеспечивают баланс: монстры — более уронные,  персонажи — более живучие и защищённые

Зависимости: math, abc


МОДУЛЬ 2

Реализует класс персонажа с ветвлением логики расчёта характеристик в зависимости от класса. Абстрактный базовый класс Unit сохранён без изменений.

Структура:

    Unit (абстрактный класс)
        - Атрибуты: strength, dexterity, constitution, wisdom, intelligence, charisma
        - Абстрактные методы: calculate_max_health(), calculate_damage(), calculate_defense()

    Character (наследуется от Unit) — игровой персонаж с классом
        - Атрибут: character_class ('warrior', 'mage', 'hunter')
        - Кэшируемые атрибуты: max_health, damage, defense
    
        Формулы (общие для всех классов):
            health = floor(constitution × 10 + strength / 2) — максимальное здоровье персонажа
        
        Формулы урона:
            warrior: floor(strength × 2.2 + constitution / 3) — урон воина
            mage:    floor(intelligence × 2.5 + wisdom / 2) — урон мага
            hunter:  floor(dexterity × 1.9 + strength / 3) — урон охотника
        
        Формулы защиты:
            warrior: floor(constitution × 1.8 + strength / 4) — защита воина
            mage:    floor(wisdom × 1.3 + intelligence / 6) — защита мага
            hunter:  floor(dexterity × 1.6 + constitution / 5) — защита охотника

Особенности:
- Используется abc.ABC для обеспечения единого интерфейса
- В конструкторе сразу вычисляются и кэшируются итоговые характеристики
- Вся логика ветвления сосредоточена внутри одного класса Character

Зависимости: abc, math


МОДУЛЬ 3

Реализует систему заклинаний и маны для игровых сущностей. Абстрактный базовый класс Unit расширен новыми атрибутами и методами, добавлен абстрактный класс Spell и конкретные реализации заклинаний.

Структура:

    Unit (абстрактный класс)
        - Атрибуты: strength, dexterity, constitution, wisdom, intelligence, charisma, spells, mana
        - Абстрактные методы: calculate_max_health(), calculate_damage(), calculate_defense()
        - Методы работы с магией: add_spell(spell), cast_spell(index)

    Spell (абстрактный класс)
        - Атрибуты: name, damage, mana_cost
        - Абстрактный метод: cast()

    Fireball, IceLance, LightningBolt (наследуются от Spell)
        - Fireball: урон 35, стоимость 15 маны
        - IceLance: урон 25, стоимость 10 маны
        - LightningBolt: урон 40, стоимость 20 маны

    Character (наследуется от Unit) — игровой персонаж с классом
        - Атрибут: character_class ('warrior', 'mage', 'hunter')
        - Кэшируемые атрибуты: max_health, damage, defense, max_mana, mana

        Формулы (общие для всех классов):
            health = constitution × 10 + strength // 2 — максимальное здоровье персонажа
    
        Формулы урона:
            warrior: floor(strength × 2.2 + constitution / 3) — урон воина
            mage:    floor(intelligence × 2.5 + wisdom / 2) — урон мага
            hunter:  floor(dexterity × 1.9 + strength / 3) — урон охотника
    
        Формулы защиты:
            warrior: floor(constitution × 1.8 + strength / 4) — защита воина
            mage:    floor(wisdom × 1.3 + intelligence / 6) — защита мага
            hunter:  floor(dexterity × 1.6 + constitution / 5) — защита охотника
        
        Формулы максимальной маны:
            warrior: floor(intelligence + strength / 2) — мана воина
            mage:    floor(intelligence × 3 + wisdom) — мана мага
            hunter:  floor(dexterity × 1.5 + wisdom / 2) — мана охотника

Особенности:
- Используется abc.ABC для обеспечения единого интерфейса в Unit и Spell
- Все расчёты возвращают целые числа (округление вниз)
- В конструкторе Character сразу вычисляются и кэшируются все характеристики, включая ману
- Метод cast_spell() проверяет наличие маны и индекса, вычитает стоимость и возвращает урон
- Вся логика ветвления по классам сосредоточена внутри одного класса Character
- Заклинания добавляются через add_spell(), применяются через cast_spell(index)

Зависимости: abc, math