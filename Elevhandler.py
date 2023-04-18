import Elev

class ElevHandler:


    def __init__(self):
        self.elevlist = []
    
    def print_meny(self):
        print("---------------------------------------")
        print("\t\t\t MENY\n")
        print("\t\t\t1. Lista elever")
        print("\t\t\t2. Lägg till elev")
        print("\t\t\t3. Ta bort elev")
        print("\t\t\t4. Spara och avsluta")

        val = input("Gör ditt val:")

        return val