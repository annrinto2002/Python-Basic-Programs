This program demonstrates the use of the private access modifier in Python. Private members are declared using a double underscore (__), which restricts direct access from outside the class.

The BankAccount class contains two private attributes: __account_number and __balance.

These attributes cannot be accessed directly from outside the class. Attempting to do so will result in an AttributeError.

A public method get_balance() is used to safely access the private balance from within the class.

The program also shows how private attributes can be accessed externally using name mangling (e.g., _BankAccount__balance). While this works, it is not recommended as it breaks encapsulation.

This example highlights how Python handles private data using name mangling to protect class internals, encouraging better encapsulation and secure coding practices.
