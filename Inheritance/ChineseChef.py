from Chef import Chef         # import the base class
class ChineseChef(Chef):      # inherits Chef class

    def make_fried_rice(self):    # this is unique to ChineseChef
        print("The chef makes fried rice")

    def make_special_dish(self):    # overwrites this function from Chef
        print("The chef makes a special dish orange chicken")