class Cat:
    name = None
    age = None
    isHppy = None

    def set_data(self, name, age, isHppy):
        self.name = name
        self.age = age
        self.isHppy = isHppy
    def get_data(self):
        print(self.name,'age:',self.age,'. Happy:',self.isHppy)


cat1 = Cat()
cat1.set_data("Bars", 3, True)


cat2 = Cat()
cat2.set_data("Jopen", 2, False)
cat2.get_data()
cat1.get_data()



