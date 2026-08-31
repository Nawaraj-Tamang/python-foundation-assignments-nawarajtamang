# Day 5 & 6: Object-Oriented Programming (OOP)

## Topics Covered

- Classes and objects ('__init__', 'self')
- Instance attributes vs class attributes
- Methods, '__str__', '@classmethod' alternative constructors
- Inheritance and 'super()', including multilevel inheritance
- Polymorphism (method overriding, shared interfaces)
- Encapsulation ('_protected' convention, '__private' name mangling, '@property')
- Abstraction ('abc.ABC', '@abstractmethod')

## Exercises

**Day 5 - OOP Basics** ('day-05-oop-basics/'):

1. Bank Account - 'BankAccount' class with deposit/withdraw methods
2. Product Inventory - class attributes vs instance attributes
3. Employee Records - looping over a list of objects
4. Student Grades - 'Student' class with a custom '__str__'
5. Book Basics - a class attribute that counts created instances
6. Shapes Polymorphism - 'Shape', 'Circle', 'Rectangle' sharing one 'area()' method
7. Bank Account Encapsulation - a private, name-mangled '__balance'
8. Book Classmethod Constructor - 'Book.from_string()' as an alternative constructor

**Day 6 - OOP Inheritance & Polymorphism** ('day-06-oop-inheritance-polymorphism/'):

1. Employee Hierarchy - 'Manager'/'SalesEmployee' overriding a base 'Employee'
2. Payment Methods - different classes sharing one 'process_payment()' interface
3. Secure Account - encapsulation via '@property' with no setter
4. Data Pipeline Components - pipeline steps chained through a shared 'run()' method
5. Vehicle Multilevel Inheritance - 'Vehicle' -> 'Car' -> 'SportsCar'
6. Payment Abstraction - an abstract 'PaymentMethod(ABC)' that can't be instantiated directly
7. Library Management System - a mini system combining all four OOP pillars

## How to Run

All exercises are notebooks inside the 'day 05&06-OOP' folder, split by difficulty:

- '01-easy-exercises.ipynb'
- '02-normal-exercise.ipynb'
- '03-hard-exercise.ipynb'
- '04-project.ipynb'

Open a notebook in VS Code with the Jupyter extension installed, then run the cells in order from top to bottom (either cell-by-cell with the play button, or via **Run All**).

## What I Learned

Day 5 was my first real shift from thinking in functions to thinking in objects, especially realizing 'self' just lets each instance track its own data independently. Day 6 built directly on that with inheritance and 'super()', which let me reuse a parent class's setup instead of rewriting it in every subclass. Polymorphism clicked once I saw the same method call working correctly across different classes without any if/else checks. The abstraction and encapsulation exercises rounded things out, showing how 'ABC' can force subclasses to implement a method, and how a private attribute is genuinely protected rather than just named that way.

## Challenges Faced

Keeping class attributes and instance attributes straight was the main early struggle, since they look similar but behave very differently. Deciding when 'super().__init__()' was actually needed took some trial and error, particularly when a subclass added extra parameters on top of the parent's. The library management challenge project was the hardest overall, since it required planning which class owned which responsibility (the item's checked-out flag, the member's borrowed list, the library's checkout logic) before writing any code.
