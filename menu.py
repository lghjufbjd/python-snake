
class Menu:
    def menu_draw(self):
        menu_els = ("1. Start game", "2. Exit")
        for menu_el in menu_els:
            print(menu_el)
    def menu_choice(self, choice):
        is_input_correct= None
        while is_input_correct is None or is_input_correct is False:
            if int(choice) == 1:
                print("Mapa")
                is_input_correct = True
            elif int(choice) == 2:
                print("Exit")
                is_input_correct = True
            else:
                print("Your input is not correct, try again")
                is_input_correct = False
                choice =input("")





