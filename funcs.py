class menus:
    def main_menu():
        print("\n[1] Display Tricks\n[2] Search for Trick\n[3] Exit")      
    def display_tricks(trick_list):
        for x in range(len(trick_list)):
            print('%d. %s'%(x+1,trick_list[x]))
    def search_trick(input,trick_list):
        if input.upper() in trick_list:
            return True

