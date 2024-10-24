class Recipe:
    def __init__(rec,name,notes):
        rec._name=name
        rec._notes=notes
    
class Ingredients(Recipe):
    def __init_subclass__(ing,quant,unit,type):
        ing._quant=quant
        ing._unit=unit
        ing._type=type

class ShoppingList(Recipe):
    def __init_subclass__(slist,amount,measure,item):
        slist._amount=amount
        slist._measure=measure
        slist._item=item

class Procedure(Recipe):
    def __init_subclass__(plist,step_num,step):
        plist._step_num=step_num
        plist._step=step
