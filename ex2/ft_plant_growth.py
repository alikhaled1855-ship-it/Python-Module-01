class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(self.name + ": " + str(self.height) + "cm, "
              + str(self.age) + " days old")

    def grow_plant(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_plant(self) -> None:
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25, 30)
    rose.show()
    start_height = rose.height

    for day in range(1, 8):
        print("=== Day " + str(day) + " ===")
        rose.grow_plant()
        rose.age_plant()
        rose.show()

    growth_week = round(rose.height - start_height, 1)
    print("Growth this week: " + str(growth_week) + "cm")
