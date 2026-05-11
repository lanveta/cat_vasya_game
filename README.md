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