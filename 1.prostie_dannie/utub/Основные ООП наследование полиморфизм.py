# наследование
class Bulding:
    __year =None
    __city =None

    def __init__(self,year,city ):
        self.city = city
        self.year = year

    def get_info(self):
        print('Year',self.year,'City',self.city)
class School (Bulding):
    pupils = 0
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print("pupils: ", self.pupils)



class Shop (Bulding):
    pass

class Hous (Bulding):
    pass


school = School(100, 2000, 'Moscow')
hous = Hous(2022, 'SPB')
shop = Shop(2011, 'Krasnodar')
school.get_info()
hous.get_info()
shop.get_info()