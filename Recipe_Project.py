class Recipe:
    def __init__(rec,name,notes):
        rec.name=name
        rec.notes=notes
    
class Ingredients(Recipe):
    def __init_subclass__(ing,quant,unit,type):
        ing.quant=quant
        ing.unit=unit
        ing.type=type

class ShoppingList(Recipe):
    def __init_subclass__(slist,amount,measure,item):
        slist.amount=amount
        slist.measure=measure
        slist.item=item

class Procedure(Recipe):
    def __init_subclass__(plist,step_num,step):
        plist.step_num=step_num
        plist.step=step
