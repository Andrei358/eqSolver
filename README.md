# eqSolver

This module provides a useful framework for solving arbitrarily sized systems of linear equations.

### How to use it

First, import the module and declare a system object

```
import eqSolver

eq = system()
```
Input the system using getSys() and passing the name of the file where the system is stored

```
eq.getSys("input.txt")
```

Finding the solution is done using solve()

```
eq.solve()
```
Print the solution to the console afterwards using print()

```
eq.printSol()
```

