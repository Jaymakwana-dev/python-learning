items = []

def add_items():
    while True:
        item = input("ENTER ITEMS : ").lower()
        items.append(item)
        print("ITEM HAS BEEN ADDED ✅")
        while True:
            choice = input("Do you you wont to Add Another items? write(Yes/No) : ").lower()
            print()
            if choice == "yes":
                break   
            elif choice == "no":
                return
            else:
                print("Enter only yes or no ❌😥")        

    
def display_items():
    if len(items) == 0:
        print("GROCERY LIST IS EMPTY ❌")
    else:
        print("GROCERY ITEMS 📃: ")
        print(items)
        print()
        # for idx ,item in enumerate(items , start=1) :
        #     print( f'{idx}.',item)

def remove_items():
    item = input("ENTER ITEM TO REMOVE IT : ").lower()
    
    if item in items:
       items.remove(item)
       print("REMOVED SUCCESSFULLY ✅")
       print()
    else:
        print("ITEM IS NOT FOUND ❌")
        print()

def check_items():
    item = input("ENTER ITEM TO CHECK : ").lower()

    if item in items:
        print("ITEMS EXISTS ✅")
    else:
        print("ITEMS DOES NOT EXISTS ❌")
print()

invalid_choice = 0

while True:
    print("----------------------------------------")
    print("----Grocery List----")
    
    print("1. Add an Items ➕")
    print("2. Display all Items 😎")
    print("3. Remove an Items 😔")
    print("4. Check whether an items Exists 🤔")
    print("5. Exit ❌")
    print()
    print("----------------------------------------")

    choice = input("Enter your Choice to run Operation: ")

    print("----------------------------------------")
    print()
    if choice == "1":
        
        add_items()
    elif choice == "2":
        
        display_items()
    elif choice == "3":
        
        remove_items()
    elif choice == "4":
        
        check_items()
    elif choice == "5":
        print("Good bye , see you soon🖤💦")
        break
    else:
        invalid_choice += 1

        print("❌❌ Invalid choice ❌❌")
        print(f"Invalid Attempts : {invalid_choice}/3 ")
        print()
        if invalid_choice >= 3:
            print("❌ You entered 3 invalid choices!")
            print()
            print("Program is exiting... 👋")
            print("Better luck next time 🤞🏼💖")
            break