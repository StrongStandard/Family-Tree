from Family_DIct import *

# main class that includes all the features and functions
class Family_Tree(Person):
    # initialise an instance of a family_tree
    def __init__(self,family_dict):
        self.family_dict = family_dict
    # returns parents a an input_person
    def get_parents(self, input_person):
        parent1 = self.family_dict[input_person].parent1
        parent2 = self.family_dict[input_person].parent2
        return parent1, parent2

    # returns parents of parents (if any) of input_person
    def get_grandparents(self,input_person):
        grandparents_list = []
        parents_list = self.get_parents(input_person)
        if parents_list[0] in self.family_dict or parents_list[1] in self.family_dict:
            grandparents_list = [self.get_parents(parents_list[0]),self.get_parents(parents_list[1])]

        return grandparents_list

    # checks for siblings and if any, returns the list of all the siblings of an input_person
    def get_sibling(self,input_person):
        siblings_list = []
        if input_person in self.family_dict:
            parents_list = self.get_parents(input_person)
            for sibling, properties in self.family_dict.items():
                if sibling != input_person:
                    if properties.parent1 == parents_list[0] and properties.parent2 == parents_list[1]:
                        siblings_list.append(sibling)
        return siblings_list

    # returns a list of children of input_person (if any)
    def get_children(self,input_person):
        children_list = []
        if input_person in self.family_dict:
            for child, parents in self.family_dict.items():
                if parents.parent1 == input_person or parents.parent2 == input_person:
                    children_list.append(child)
        return children_list

    # returns a list of uncles/aunties of input_person (if any)
    def get_uncles(self,input_person):
        uncle_list = []
        parents_list = self.get_parents(input_person)
        uncle_list = self.get_sibling(parents_list[0])
        uncle_list.extend(self.get_sibling(parents_list[1]))
        return uncle_list

    # returns a list of cousins of an input peron (if any)
    def get_cousin(self,input_person):
        cousins_list = []
        if input_person in self.family_dict:
            parents_list = self.get_parents(input_person)
            siblings_list = self.get_sibling(parents_list[0])
            if len(parents_list) > 1:
                siblings_list.extend(self.get_sibling(parents_list[1]))
            # for loop that goes through the list of siblings and get children of each sibling and they are cousins
            for s in siblings_list:
                cousins_list.extend(self.get_children(s))
        return cousins_list

    # returns a spouse of an input person
    def get_spouse(self,input_person):
        spouse = ""
        for name, properties in self.family_dict.items():
            if properties.parent1 == input_person:
                spouse = properties.parent2
            elif properties.parent2 == input_person:
                spouse = properties.parent1
        return spouse

    # displays all family birthdays (inncluding years)
    def display_family_birthdays(self):
        for name, properties in self.family_dict.items():
            print(name + ": " + properties.birthdate)

    # creates a sorted (by month and day) family calendar (excluding years)
    def display_birthday_calendar(self):
        birthday_dict = {}
        for name, properties in self.family_dict.items():
            if properties.birthdate[5:] in birthday_dict:
                birthday_dict[properties.birthdate[5:]].append(name)
            else:
                birthday_dict[properties.birthdate[5:]] = [name]
        sorted_months = sorted(birthday_dict.keys())

        for month in sorted_months:
            names = ", ".join(birthday_dict[month])  # Join names with commas
            print(f"{month}: {names}")

    # display a list of people who have children and shows how many children they have, than average the amount of children per person
    def display_average_number_of_children(self):
        children_per_person = {}
        average = 0
        for name, properties in self.family_dict.items():
            if len(self.get_children(name)) != 0:
                # Ensure the key exists and has a list as its value
                children_per_person.setdefault(name, [])
                children_per_person[name].extend(self.get_children(name))  # Use extend instead of append

        for key in children_per_person:
            print(f"{key}: {': '.join(str(len(children_per_person[key])))}")
            average += (len(children_per_person[key]))
        print("\nThe average number of children per person:", average//len(children_per_person))

    # displays people who have died with their age of death, than makes an average age of death
    def display_average_death(self):
        dead_dict = {}
        average = 0
        for person, properties in self.family_dict.items():
            if properties.deathdate != "null":
                if person not in dead_dict:
                    dead_dict[person] = int(properties.deathdate[:4]) - int(properties.birthdate[:4])

        for person in dead_dict:
            print(f"{person}: {"".join(str(dead_dict[person]))}")
            average += dead_dict[person]
        print("\nThe average age of death:", average//len(dead_dict.keys()))

# creates and instance of a family object
family = Family_Tree(family_dict)

#prints the recorded family for user to see
print("\nList of recorded family.\n")
for name in family_dict:
    print(name)
task = ''
while task != "x":

# input menu for user to choose from
    task = input("""\nWhat would you like to do?\n
Press 1 to show parents
Press 2 to show grandparents.
Press 3 to show siblings.
Press 4 to show cousins.
Press 5 to display immediate family.
Press 6 to display extended family.
Press 7 to display all family birthdays.
Press 8 to display the family calendar.
Press 9 to find an average number of children.
Press 10 to find an average age of death.
Press x to end.\n""")


    if task == "1":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:

            print(family.get_parents(input_person))
        else:
            print("No data recorded.")

    if task == "2":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:
            print(family.get_grandparents(input_person))
        else:
            print("No data recorded.")



    if task == "3":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:
            if len(family.get_sibling(input_person)) < 1:
                print("No data recorded.")
            else:
                print(family.get_sibling(input_person))
        else:
            print("No data recorded.")

    # get cousin
    if task == "4":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:
            if len(family.get_cousin(input_person)) < 1:
                print("No data recorded.")
            else:
                print(family.get_cousin(input_person))
        else:
            print("No data recorded.")

    if task == "5":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:
            print("Parents: ",family.get_parents(input_person))
            print("Siblings: ",family.get_sibling(input_person))
        print("Spouse: ",family.get_spouse(input_person))
        print("Children: ",family.get_children(input_person))

    if task == "6":
        input_person = input("Enter the full name: ")
        if input_person in family.family_dict:
            print("Grandparents: ", family.get_grandparents(input_person))
            print("Uncles/Aunties: ", family.get_uncles(input_person))
            print("Cousins: ", family.get_cousin(input_person))
        else:
            print("No data recorded.")

    if task == "7":
        family.display_family_birthdays()

    if task == "8":
        family.display_birthday_calendar()
    if task == "9":
        family.display_average_number_of_children()

    if task == "10":
        family.display_average_death()

    if task == "x":
        exit()