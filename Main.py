import Elevhandler

looping = True

Skola = Elevhandler.ElevHandler()



while looping:
    Val = Skola.print_meny()
    
    if (Val == "1"):
        print("lista elever")
    
    elif (Val == "2"):
        namn = input("Mata in namnet:")
        utb = input("Mata in utbildning")
        tel = input("Mata in telfonnummer"")
    
    elif (Val == "3"):
        print("Ta bort elev")

    elif (Val == "4"):
        break