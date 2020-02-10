#function can be overrided with same def functions as imported file
from chef1 import chef1
class chef2(chef1):
    
    def make_chicken_2 (self):
        print("The chef makes chicken_thai!! ")

    def make_salad_2(self):
        print("The chef makes salad_thai! ")