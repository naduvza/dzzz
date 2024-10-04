import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.money = 100

    def to_study(self):
        print("Time to study")
        self.progress += 0.15
        self.gladness -= 4

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 10

    def to_work(self):
        print("Working...")
        self.money += 50
        self.gladness -= 3

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
        elif self.money < 0:
            print("Bankrupt…")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")

    def auto_manage(self):
        if self.money < 20:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 20:
            self.to_chill()
        else:
            self.to_sleep()

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        self.auto_manage()
        self.end_of_day()
        self.is_alive()


nick = Student(name="Nick")
for day in range(365):
    if not nick.alive:
        break
    nick.live(day)