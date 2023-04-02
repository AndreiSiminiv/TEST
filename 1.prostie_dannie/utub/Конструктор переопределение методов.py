class Cat:
    name = None
    age = None
    isHppy = None

    def __init__(self, name={'Не заполнено'}, age=None, isHppy={'Не заполнено'}):
        self.set_data(name, age, isHppy)
        self.get_data()

    def set_data(self, name= None, age = None, isHppy = None):
        self.name = name
        self.age = age
        self.isHppy = isHppy
    def get_data(self):
        print(self.name,'age:',self.age,'. Happy:',self.isHppy)


cat1 = Cat("Bars", 3,True )
cat2 = Cat("Jopen", 2 )






