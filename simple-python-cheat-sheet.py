def display_header():
    print("\n" + "=" * 60)
    print("PYTHON CHEAT SHEET".center(60))
    print("=" * 60)

def display_main_menu():
    print("\nPlease select from the following options:\n")
    print("[1] Math Operations")
    print("[2] Variables & Data Types")
    print("[3] Conditional Statements")
    print("[4] Loops")
    print("[5] Lists")
    print("[6] Dictionaries")
    print("[7] Tuples")
    print("[8] Functions")
    print("[9] Help")
    print("[0] Exit")

def display_continue_menu():
    print("\n[1] Continue")
    print("[0] Main Menu")
    choice = input("\nEnter your choice: ")
    return choice

def display_help():
    print("\n" + "=" * 60)
    print("HELP".center(60))
    print("=" * 60)
    print("\nThis is a simple Python cheat sheet program.")
    print("Select a topic number to view information about that topic.")
    print("After viewing a topic, you can continue or return to the main menu.")
    print("Select '0' to exit the program.")

def display_math_operations():
    print("\n" + "=" * 60)
    print("MATH OPERATIONS".center(60))
    print("=" * 60)
    
    print("\nBasic Arithmetic:")
    print("a + b    # Addition")
    print("a - b    # Subtraction")
    print("a * b    # Multiplication")
    print("a / b    # Division (returns float)")
    print("a // b   # Floor division (returns int)")
    print("a % b    # Modulo (remainder)")
    print("a ** b   # Exponentiation (a to the power of b)")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nMath Functions (from math module):")
        print("import math")
        print("math.sqrt(x)     # Square root")
        print("math.ceil(x)     # Round up to nearest integer")
        print("math.floor(x)    # Round down to nearest integer")
        print("math.pi          # Pi constant")
        print("math.e           # e constant")
        print("math.sin(x)      # Sine of x (in radians)")
        print("math.cos(x)      # Cosine of x (in radians)")
        print("math.tan(x)      # Tangent of x (in radians)")
        print("math.log(x)      # Natural logarithm of x")
        print("math.log10(x)    # Base-10 logarithm of x")

def display_variables():
    print("\n" + "=" * 60)
    print("VARIABLES & DATA TYPES".center(60))
    print("=" * 60)
    
    print("\nVariable Assignment:")
    print("name = 'John'     # String")
    print("age = 30          # Integer")
    print("height = 1.75     # Float")
    print("is_student = True # Boolean")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nChecking Types:")
        print("type(name)           # Returns the type of the variable")
        print("isinstance(age, int) # Checks if age is an integer")
        print("\nType Conversion:")
        print("str(123)        # Convert to string: '123'")
        print("int('456')      # Convert to integer: 456")
        print("float('3.14')   # Convert to float: 3.14")
        print("bool(0)         # Convert to boolean: False")

def display_conditionals():
    print("\n" + "=" * 60)
    print("CONDITIONAL STATEMENTS".center(60))
    print("=" * 60)
    
    print("\nIf-Elif-Else Statement:")
    print("if condition1:")
    print("    # code to run if condition1 is True")
    print("elif condition2:")
    print("    # code to run if condition1 is False and condition2 is True")
    print("else:")
    print("    # code to run if all conditions are False")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nComparison Operators:")
        print("a == b    # Equal to")
        print("a != b    # Not equal to")
        print("a > b     # Greater than")
        print("a < b     # Less than")
        print("a >= b    # Greater than or equal to")
        print("a <= b    # Less than or equal to")
        print("\nLogical Operators:")
        print("and    # True if both conditions are True")
        print("or     # True if at least one condition is True")
        print("not    # Inverts True/False value")

def display_loops():
    print("\n" + "=" * 60)
    print("LOOPS".center(60))
    print("=" * 60)
    
    print("\nFor Loop:")
    print("for item in iterable:")
    print("    # code to execute for each item")
    print("\nExample:")
    print("for i in range(5):")
    print("    print(i)  # Prints 0, 1, 2, 3, 4")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nWhile Loop:")
        print("while condition:")
        print("    # code to execute while condition is True")
        print("\nExample:")
        print("count = 0")
        print("while count < 5:")
        print("    print(count)")
        print("    count += 1  # Prints 0, 1, 2, 3, 4")
        print("\nLoop Control:")
        print("break     # Exit the loop completely")
        print("continue  # Skip to the next iteration")
        print("pass      # Do nothing (placeholder)")

def display_lists():
    print("\n" + "=" * 60)
    print("LISTS".center(60))
    print("=" * 60)
    
    print("\nCreating Lists:")
    print("empty_list = []")
    print("numbers = [1, 2, 3, 4, 5]")
    print("mixed = [1, 'hello', True, 3.14]")
    print("nested = [1, [2, 3], [4, [5, 6]]]")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nList Operations:")
        print("numbers.append(6)      # Add item to end")
        print("numbers.insert(0, 0)   # Insert at index")
        print("numbers.pop()          # Remove and return last item")
        print("numbers.remove(3)      # Remove first occurrence of value")
        print("del numbers[0]         # Delete item at index")
        print("len(numbers)           # Get length of list")
        print("sorted(numbers)        # Return sorted copy")
        print("numbers.sort()         # Sort list in place")
        print("numbers.reverse()      # Reverse list in place")
        
        choice = display_continue_menu()
        if choice == "1":
            print("\nList Slicing:")
            print("numbers[1:3]           # [2, 3]   (start:stop)")
            print("numbers[:2]            # [1, 2]   (beginning to index)")
            print("numbers[2:]            # [3, 4, 5] (index to end)")
            print("numbers[-1]            # 5 (last item)")
            print("numbers[-2:]           # [4, 5] (last two items)")
            print("\nList Comprehensions:")
            print("[x*2 for x in range(5)]            # [0, 2, 4, 6, 8]")
            print("[x for x in range(10) if x % 2==0] # [0, 2, 4, 6, 8]")

def display_dictionaries():
    print("\n" + "=" * 60)
    print("DICTIONARIES".center(60))
    print("=" * 60)
    
    print("\nCreating Dictionaries:")
    print("empty_dict = {}")
    print("person = {'name': 'John', 'age': 30, 'city': 'New York'}")
    print("grades = dict(alice=95, bob=82, charlie=88)")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nAccessing and Modifying:")
        print("person['name']                # Get value: 'John'")
        print("person['email'] = 'j@ex.com'  # Add new key-value pair")
        print("person['age'] = 31            # Modify existing value")
        print("del person['city']            # Delete a key-value pair")
        print("person.get('phone')           # Returns None if key doesn't exist")
        print("person.get('phone', 'N/A')    # Returns 'N/A' if key doesn't exist")
        
        choice = display_continue_menu()
        if choice == "1":
            print("\nDictionary Methods:")
            print("person.keys()     # dict_keys object with all keys")
            print("person.values()   # dict_values object with all values")
            print("person.items()    # dict_items object with (key, value) pairs")
            print("person.update(other_dict)  # Merge dictionaries")
            print("person.pop('age') # Remove and return value for key")
            print("person.clear()    # Remove all items")
            print("\nDictionary Comprehensions:")
            print("{x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}")

def display_tuples():
    print("\n" + "=" * 60)
    print("TUPLES".center(60))
    print("=" * 60)
    
    print("\nCreating Tuples:")
    print("empty_tuple = ()")
    print("single_item = (1,)  # Note the comma")
    print("numbers = (1, 2, 3, 4, 5)")
    print("mixed = (1, 'hello', True)")
    print("nested = (1, (2, 3), (4, 5))")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nTuple Operations:")
        print("numbers[0]      # Access item: 1")
        print("numbers[1:3]    # Slice: (2, 3)")
        print("len(numbers)    # Length: 5")
        print("3 in numbers    # Check membership: True")
        print("numbers.count(1)  # Count occurrences: 1")
        print("numbers.index(3)  # Find index of value: 2")
        print("\nTuples vs Lists:")
        print("- Tuples are immutable (cannot be changed after creation)")
        print("- Tuples can be used as dictionary keys, lists cannot")
        print("- Tuples are slightly faster than lists for iteration")
        print("- Use tuples for fixed data, lists for changeable data")

def display_functions():
    print("\n" + "=" * 60)
    print("FUNCTIONS".center(60))
    print("=" * 60)
    
    print("\nDefining Functions:")
    print("def greet(name):")
    print("    return f'Hello, {name}!'")
    print("\ndef calculate_total(items, tax_rate=0.1):")
    print("    subtotal = sum(items)")
    print("    tax = subtotal * tax_rate")
    print("    return subtotal + tax")
    
    choice = display_continue_menu()
    if choice == "1":
        print("\nFunction Arguments:")
        print("# Positional arguments")
        print("greet('Alice')  # Hello, Alice!")
        print("\n# Keyword arguments")
        print("calculate_total([10, 20, 30], tax_rate=0.05)")
        print("\n# Variable-length arguments")
        print("def add_all(*numbers):")
        print("    return sum(numbers)")
        print("\nadd_all(1, 2, 3, 4)  # 10")
        
        choice = display_continue_menu()
        if choice == "1":
            print("\n# Variable-length keyword arguments")
            print("def user_info(**kwargs):")
            print("    return kwargs")
            print("\nuser_info(name='Alice', age=30, city='Boston')")
            print("# Returns: {'name': 'Alice', 'age': 30, 'city': 'Boston'}")
            print("\n# Lambda (Anonymous) Functions:")
            print("multiply = lambda x, y: x * y")
            print("multiply(5, 3)  # 15")

def main():
    while True:
        display_header()
        display_main_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == "0":
            print("\nThank you for using the Python Cheat Sheet. Goodbye!")
            break
        elif choice == "1":
            display_math_operations()
        elif choice == "2":
            display_variables()
        elif choice == "3":
            display_conditionals()
        elif choice == "4":
            display_loops()
        elif choice == "5":
            display_lists()
        elif choice == "6":
            display_dictionaries()
        elif choice == "7":
            display_tuples()
        elif choice == "8":
            display_functions()
        elif choice == "9":
            display_help()
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
