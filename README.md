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