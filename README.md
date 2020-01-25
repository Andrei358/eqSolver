# eqSolver

This module provides a useful framework for solving arbitrarily sized systems of linear equations.

### How to use it

First, import the module and declare a system object

```
import eqSolver

eq = system()
```
Input the system using getSys() and pass the name of the file where the system is 

```
eq.getSys("input.txt")
```

Finding the solution is done using solve()

```
eq.solve()
```
Print the solution to the console afterwards using printSol()

```
eq.printSol()
```
### How to represent systems

The following is an example of how a system must be represented in the input file

Actual system | Representation
--- | --- 
2x + 3y + 4z = 5 <br /> 3x - 4y = -5 |2 3 <br />  2 3 4 5 <br />  3 4 0 -5
