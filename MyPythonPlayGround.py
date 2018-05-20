class MyPythonPlayGround:
    # Integers and Floats
    # The format here is: Variable Name = Variable Value
    answer = 42

    # We can also have floats
    pi = 3.14159

    # Don't worry about conversion
    print(answer + pi)  # 45.14159

    # Casting
    int(pi) == 3
    float(answer) == 42.0

    # Strings are defined using single, double or triple quotes
    'Hello World' == "Hello World" == """Hello World"""

    # Useful Methods
    print("hello".capitalize())
    print("hello".replace("e", "a"))
    print("hello".isalpha())
    print("123".isdigit())
    print("some, csv, example".split(","))

    # String format function
    name = "Artemas"
    machine = "HAL"
    print("Nice to meet you {0}. I am {1}".format(name, machine))
    print(f"Nice to meet you {name}. I am {machine}")  # Notice the 'f' at the beginning of the String
