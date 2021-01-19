
class Car:

    def __init__(self, model, brand, color,speed):
        self.model = model
        self.brand = brand
        self.color = color
        self._state = 'not_moving'
        self._motor = Motor(cylinders=4)
        self.speed = 0

    def speed_up(self, type='slow'):
        if type =='fast':
            self._motor.inject_gasoline(10)
        else:
            self.motor.inject_gasoline(3)

        self._state ='is_moving'
    
    def break(self,type='slow'):
        if self.speed==0:
            self.state = 'not_moving'
            return self._state
        if type == 'slow':
            self.speed -= 1
        else:
            self.speed -=3

    def make_a_right(self,type='slow'):
        if type == 'slow':
            self.speed = (5)
        else:
            self.speed =(10)
        
    def make_a_left (self,type='slow'):
        if type == 'slow':
            self.speed = (5)
        else:
            self.speed= (10)

class Motor:

    def __init__(self,cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline(self,amount):
        pass


class Lights:

    def __init__(self,material, light_bulds):
        self.material = material
        self.light_bulds = light_bulds
        self._state = 'off'
    
    def turn_on(self):
        self.turn_on= True

    def turn_off (self):
        self.turn_on= False

class A_C:

    def __init__(self, temperature,cool,dry, heat,):
        self.temperature = temperature
        self.cool = cool
        self.dry = dry
        self.heat = heat
    
     def turn_on(self):
        self.turn_on= True

    def turn_off (self):
        self.turn_on= False
