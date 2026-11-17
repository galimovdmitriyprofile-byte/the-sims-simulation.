"""
Практическое задание №2
Тема: Работа с несколькими классами. Разработка The Sims
"""


class House:
    """Дом предоставляет персонажу места и предметы для действий."""

    def __init__(self, name):
        self.name = name
        self.food = 3
        self.comfort = 2

    def cook_meal(self, person):
        if self.food <= 0:
            print("В холодильнике закончилась еда.")
            return
        self.food -= 1
        person.eat(35)
        print(f"{person.name} приготовил(а) еду и поел(а).")

    def provide_sleep(self, person):
        person.sleep(45)
        print(f"{person.name} поспал(а) в своей кровати.")

    def provide_rest(self, person):
        person.relax(self.comfort)
        print(f"{person.name} отдохнул(а) дома.")


class Person:
    """Персонаж имеет потребности и взаимодействует с домом."""

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.energy = 60
        self.hunger = 60
        self.mood = 60

    def eat(self, amount):
        self.hunger = min(100, self.hunger + amount)
        self.mood = min(100, self.mood + 5)

    def sleep(self, amount):
        self.energy = min(100, self.energy + amount)
        self.mood = min(100, self.mood + 5)

    def relax(self, comfort):
        self.energy = min(100, self.energy + 10)
        self.mood = min(100, self.mood + comfort * 5)

    def perform_daily_activity(self):
        self.energy = max(0, self.energy - 15)
        self.hunger = max(0, self.hunger - 15)
        self.mood = max(0, self.mood - 5)

    def show_status(self):
        print(f"\nСостояние персонажа: {self.name}")
        print(f"Энергия: {self.energy}/100")
        print(f"Сытость: {self.hunger}/100")
        print(f"Настроение: {self.mood}/100")


class Simulation:
    """Управляет ходом симуляции и взаимодействием объектов."""

    def __init__(self, person, house):
        self.person = person
        self.house = house
        self.day = 1

    def run_day(self):
        print("=" * 42)
        print(f"СИМУЛЯЦИЯ THE SIMS — ДЕНЬ {self.day}")
        print(f"Дом: {self.house.name}")
        print("=" * 42)

        self.person.show_status()

        print("\nУтро: персонаж начинает свой день.")
        self.person.perform_daily_activity()

        print("\nДень: пора позаботиться о потребностях.")
        self.house.cook_meal(self.person)
        self.house.provide_rest(self.person)

        print("\nВечер: персонаж готовится ко сну.")
        self.person.perform_daily_activity()
        self.house.provide_sleep(self.person)

        print("\nИтог дня:")
        self.person.show_status()
        print(f"Осталось порций еды: {self.house.food}")
        self.day += 1


def main():
    house = House("Уютный дом")
    person = Person("Алекс", house)
    simulation = Simulation(person, house)
    simulation.run_day()


if __name__ == "__main__":
    main()
