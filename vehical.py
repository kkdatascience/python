class vehical :
 def vehical_info(self):
        self.vehical = 'Muruthi'
    print(self.vehical)
    
class car(vehical):
 def car_info(self,brand_name, no_of_doors):
    vehical = super().vehical_info()
              print('car name:' , brand_name  , 'No of doors:', no_of_doors, 'vehical_name:', self.vehical)

class sport_car(car):
    def sport_car_info(self):
        print('final car')

s_car = sport_car()
s_car.vehical_info()
s_car.car_info('Swift',5)