print("====== SMART CALCULATOR ======")
History = []

def addition():
    result  = num1 + num2
    entry = f"{num1} + {num2} = {result}"
    History.append(entry)
    print(f"Result = Addition of {num1} and {num2} is : {result}")
    print()
    print("===================================")
    
def subtraction():
    result = num1 - num2
    entry = f"{num1} - {num2} = {result}"
    History.append(entry)
    print(f"Result = Subtraction of {num1} and {num2} is : {result}")
    print()
    print("===================================")

def multiplication():
    result = num1 * num2
    entry = f"{num1} * {num2} = {result}"
    History.append(entry)
    print(f"Result = Multiplication of {num1} and {num2} is : {result}")
    print()
    print("===================================")
    
def division():
    if num2 == 0:
        print("Error: Division by zero is not allowed.(ZeroDivisionError) ❌")
    else:
        result = num1 / num2
        entry = f"{num1} / {num2} = {result}"
        History.append(entry)
        print(f"Result = Division of {num1} and {num2} is : {result}")
        print()
    print("===================================")
    
def display_history():
    print("====== History of Calculation ======")
    if History:
        for entry in History:
            print(entry)
    else:
        print("No calculations performed yet.")
    

while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print()
    except ValueError:
        print("Invalid input. Please enter valid numbers. ❌")
        continue

    print()
    print("===================================")  
    print("Here are the operations you can perform: ")
    
    print("----------------------------------------")
    print()
    print("1. Addition ➕")
    print("2. Subtraction ➖")
    print("3. Multiplication ✖️")
    print("4. Division ➗")
    print("5. Display History (Press 'H' to view) 📜")
    print("6. Exit (Press 'E' to exit) ❌")
    
    print()
    choice = input("Enter your Choice to run Operation: ").lower()
    
    print("----------------------------------------")
    print() 
    
    if choice == "+":
        addition()
    elif choice == "-":
        subtraction()
    elif choice == "*":
        multiplication()
    elif choice == "/":
        division()
    elif choice == "h".lower():
        display_history()
    elif choice == "e".lower():
        print("Thank you for using Smart Calculator! ✅")
        break
    else:
        print("Invalid choice. Please enter a valid option.(+, -, *, /, H to view history, or E to exit) ❌")
        restart_choice = input("Do you want to calculate again ? (Y/N): ").lower()
        if restart_choice == "y":
            continue
        if restart_choice == "n":
            print("Thank you for using Smart Calculator! ✅")
            break




