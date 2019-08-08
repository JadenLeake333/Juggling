class menus:
    def main_menu():
        print("\n[1] Display Tricks\n[2] Search for Trick\n[3] Add a learned trick\n[4] View Learned Tricks\n[5] Exit")      
    def display_tricks(trick_list):
        for x in range(len(trick_list)):
            print('%d. %s'%(x+1,trick_list[x]))
    def search_trick_website(input,trick_list,links):
        if input in trick_list:
            url = "http://libraryofjuggling.com/%s" %(links.get(input))
            return url
        else:
            print("\nCould not find that trick!")
    def add_tricks(input,trick_list,links,catalog):
        if input in trick_list:
            catalog.write('%s\n'%input)
            print("\n%s has been added and saved!" %input)
        else:
            print("\nCould not find that trick to add!")
    def view_tricks(catalog):
        print(catalog.readlines())


