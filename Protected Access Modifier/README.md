This program demonstrates the use of protected members in Python. Protected attributes are defined using a single underscore prefix (e.g., _name, _revenue).

In Python, protected members can be accessed:

Within the class where they are defined.

In subclasses that inherit from the class.

Although they can be accessed from outside the class, it is not recommended, as it's against the intended use.

The program includes:

A Company class with protected attributes _name and _revenue.

A Branch subclass that accesses these protected members.

An object of Branch that demonstrates access from both inside the class and (not recommended) directly from outside the class.
