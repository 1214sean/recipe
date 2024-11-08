import os.path

class Recipe:
    def __init__(self,name,notes):
        self._name=name
        self._notes=notes

    def get_name(self):
        return self._age
    
    def set_name(self,nm):
        self._name = nm
    
    def get_notes(self):
        return self._notes
    
    def set_notes(self,nt):
        self._notes = nt
    
class Ingredients(Recipe):
    def __init_subclass__(self,quant,unit,type):
        self._quant=quant
        self._unit=unit
        self._type=type

    def get_quant(self):
        return self._quant
    
    def set_quant(self,qt):
        self._quant = qt

    def get_unit(self):
        return self._unit
    
    def set_unit(self,un):
        self._unit = un
    
    def get_type(self):
        return self._type
    
    def set_type(self, ty):
        self._type = ty

class ShoppingList(Recipe):
    def __init_subclass__(self,amount,measure,item):
        self._amount=amount
        self._measure=measure
        self._item=item

    def get_amount(self):
        return self._amount

    def set_amount(self,am):
        self._amount = am

    def get_measure(self):
        return self._measure
    
    def set_measure(self,ms):
        self._measure = ms

    def get_item(self):
        return self._item
    
    def set_item(self,it):
        self._item = it

class Procedure(Recipe):
    def __init_subclass__(self,step_num,step):
        self._step_num=step_num
        self._step=step

    def get_step_num(self):
        return self._step_num
    
    def set_step_num(self,sn):
        self._step_num = sn

    def get_step(self):
        return self._step
    
    def set_step(self,st):
        self._step = st

def main():
    if os.path.exists("Recipe_Database.txt"):
        with open("Recipe_Database.txt", "r") as database:
            recipe_list = []
            line = database.readline()
            while line:
                recipe_list.append(str(line).strip())
                line = database.readline()
        database.close()
    else:
        database = open("Recipe_Database.txt", "x")

    print(recipe_list)

main()
