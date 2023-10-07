language = input("Choose a language! (options: English, Hungarian)\n")
print("")
if language == "Magyar" or language == "magyar" or language == "Hungarian" or language == "hungarian":

    def osztas():
        print('Osztás:')
        print('')
        n = input('Osztandó: ')
        d = input('Osztó: ')
        print("")

        try:
                ans = float(n)/float(d)
        except ZeroDivisionError:
            print('Nullával nem lehet osztani!\n')
            osztas()
        except ValueError:
            print('Betüvel nem lehet osztani!\n')
            osztas()
        else:
            print(f"Az eredmény: {ans}")
            print("")

    def szorzas():
        print('Szorzás: \n')
        n = input('Szorzandó: ')
        d = input('Szorzó: ')
        print("")

        try:
            ans = float(n)*float(d)
        except ValueError:
            print('Betüket nem lehet összeadni!\n')
            szorzas()
        else:
            print(f"Az eredmény: {ans}")
            print("")

    def osszeadas():
        print('Összeadás: \n')
        print('')
        n = input('Elsö tag: ')
        d = input('Második tag: ')
        print("")

        try:
            ans = float(n)+float(d)
        except ValueError:
            print('Betüket nem lehet összeadni!\n')
            osszeadas()
        else:
            print(f"Az eredmény: {ans}")
            print("")

    def kivonas():
        print('Kivonás: \n')
        print('')
        n = input('Alap: ')
        d = input('Kivonandó: ')
        print("")

        try:
                    ans = float(n)-float(d)
        except ValueError:
            print('Betüvel nem lehet osztani!\n')
            kivonas()
        else:
            print(f"Az eredmény: {ans}")
            print("")

    def osztas_utani_maradek():
        print('Osztás utáni maradék (Módusz):\n')
        print('')
        n = input('Osztandó: ')
        d = input('Osztó: ')
        print("")

        try:
            ans = float(n)%float(d)
        except ValueError:
            print('Betüvel nem lehet osztani!\n')
            osztas_utani_maradek()
        else:
            print(f"Az eredmény: {ans}")
            print("")

    def szazalekszamitas():
        print('Százalékszámítás:\n')
        print('')
        n = input('Százalékalap: ')
        d = input('Százalékláb: ')
        print("")

        try:
            ans = float(n)/100*float(d)
        except ValueError:
            print('Betüvel nem lehet elvégezni ezt a műveletet!\n')
            szazalekszamitas()
        else:
            print(f"Százalékérték: {ans}")
            print("")

    while True:
        muvelet = input("Milyen műveletet szeretnél végrehajtani?: ")
        print("")
        if muvelet == "Osztás" or muvelet == "osztás":

            osztas()

        elif muvelet == "Szorzás" or muvelet == "szorzás":
                    
            szorzas()

        elif muvelet == "Összeadás" or muvelet == "összeadás":

            osszeadas()

        elif muvelet == "Kivonás" or muvelet == "kivonás":
                        
            kivonas()

        elif muvelet == "Osztás utáni maradék" or muvelet == "osztás utáni maradék":
                        
            osztas_utani_maradek()

        elif muvelet == "Százalékszámítás" or muvelet == "százalékszámítás":
                        
            szazalekszamitas()


        else:
            print("Sajnost ezt a műveletet nem ismerem.")
            print("")


elif language == "Angol" or language == "angol" or language == "English" or language == "english":

    def division():
        print('Division:')
        print('')
        n = input('Divinded: ')
        d = input('Divisor: ')
        print("")

        try:
            ans = float(n)/float(d)
        except ZeroDivisionError:
            print('You cannot divide by zero\n')
            division()
        except ValueError:
            print('Wrong input format!\n')
            division()
        else:
            print(f"Quotient: {ans}")
            print("")

    def addition():
        print('Addition: \n')
        n = input('First tag: ')
        d = input('Second tag: ')
        print("")

        try:
            ans = float(n)+float(d)
        except ValueError:
            print('Wrong input format!\n')
            addition()
        else:
            print(f"Result: {ans}")
            print("")

    def multiplication():
        print('Multiplication: \n')
        print('')
        n = input('Factor 1: ')
        d = input('Factor 2: ')
        print("")

        try:
                ans = float(n)*float(d)
        except ValueError:
            print("Wrong input format!\n")
            multiplication()
        else:
            print(f"Result: {ans}")
            print("")

    def subtraction():
        print('Subtraction: \n')
        print('')
        n = input('Basis:: ')
        d = input('Substracted: ')
        print("")

        try:
                ans = float(n)-float(d)
        except ValueError:
            print('Wrong input format!\n')
            subtraction()
        else:
            print(f"Result: {ans}")
            print("")

    def remainder_after_division():
        print('Remainder after division (Modulus):\n')
        print('')
        n = input('Basis: ')
        d = input('Divisor: ')
        print("")

        try:
            ans = float(n)%float(d)
        except ValueError:
            print('Wrong input format!\n')
            remainder_after_division()
        except ZeroDivisionError:
            print('You cannot divide by zero\n')
            remainder_after_division()
        else:
            print(f"Result: {ans}")
        print("")

    def szazalekszamitas():
        print('Percentage:\n')
        print('')
        n = input('Basis: ')
        d = input('How many percentage: ')
        print("")

        try:
            ans = float(n)/100*float(d)
        except ValueError:
            print('Wrong input format!\n')
            szazalekszamitas()
        else:
            print(f"Result: the {d}% of {n} is {ans}")
            print("")

    while True:
        muvelet = input("Select calculation method: \nOptions:\n Divisions\n Multiplication\n Addition\n Subtraction\n Remainder after division (modulus)\n Percentage\n")
        print("")
        if muvelet == "Division" or muvelet == "division":

            division()

        elif muvelet == "Multiplication" or muvelet == "division":
                    
            multiplication()

        elif muvelet == "Addition" or muvelet == "addition":
            
            addition()

        elif muvelet == "Subtraction" or muvelet == "subtraction":
                        
            subtraction()

        elif muvelet == "Remainder after division" or muvelet == "remainder after division" or muvelet == "Modulus" or muvelet == "modulus":
                        
            remainder_after_division()

        elif muvelet == "Percentage" or muvelet == "percentage":
                        
            szazalekszamitas()

        else:
            print("Unfortunately, I don't know this operation.")
            print("")

else:
    print("I don't know this language.")
    print("")
