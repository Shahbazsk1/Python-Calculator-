# Python-Calculator-
An interactive command-line calculator built in Python that performs basic arithmetic operations like addition, subtraction, multiplication, and division. 
The calculator supports chained operations where users can continue calculations with the previous result or start a new one.

✅Step 1: Import ASCII Art
Imported a logo from a custom art.py file to display a cool calculator banner when the program starts.

✅ Step 2: Define Arithmetic Functions
Created four core functions:
add(n1, n2)
subtract(n1, n2)
multiply(n1, n2)
divide(n1, n2)

✅ Step 3: Store Functions in a Dictionary
Mapped operators (+, -, *, /) to their respective functions in a dictionary called operations.
<br>Example: operations["+"] = add

✅ Step 4: Build the Main Calculator Logic
<br>a.Asked the user for the first number.
<br>b.Displayed available operations and prompted for one.
<br>c.Asked for the second number.
<br>d.Performed the calculation using the chosen operation from the dictionary.
<br>e.Displayed the result.

✅ Step 5: Loop for Continuous Calculation
Gave the user the option to continue with the previous result.
<br>-If "yes", looped with the new value as num1.
<br>-If "no", restarted the calculator from scratch using recursion.
