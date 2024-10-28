class Recipe:
    def __init__(rec,name,notes):
        rec._name=name
        rec._notes=notes

    def get_name(rec):
        return rec._age
    
    def set_name(rec,nm):
        rec._name = nm
    
    def get_notes(rec):
        return rec._notes
    
    def set_notes(rec,nt):
        rec._notes = nt
    
class Ingredients(Recipe):
    def __init_subclass__(ing,quant,unit,type):
        ing._quant=quant
        ing._unit=unit
        ing._type=type

    def get_quant(ing):
        return ing._quant
    
    def set_quant(ing,qt):
        ing._quant = qt

    def get_unit(ing):
        return ing._unit
    
    def set_unit(ing,un):
        ing._unit = un
    
    def get_type(ing):
        return ing._type
    
    def set_type(ing, ty):
        ing._type = ty

class ShoppingList(Recipe):
    def __init_subclass__(slist,amount,measure,item):
        slist._amount=amount
        slist._measure=measure
        slist._item=item

    def get_amount(slist):
        return slist._amount

    def set_amount(slist,am):
        slist._amount = am

    def get_measure(slist):
        return slist._measure
    
    def set_measure(slist,ms):
        slist._measure = ms

    def get_item(slist):
        return slist._item
    
    def set_item(slist,it):
        slist._item = it

class Procedure(Recipe):
    def __init_subclass__(plist,step_num,step):
        plist._step_num=step_num
        plist._step=step

    def get_step_num(plist):
        return plist._step_num
    
    def set_step_num(plist,sn):
        plist._step_num = sn

    def get_step(plist):
        return plist._step
    
    def set_step(plist,st):
        plist._step = st
