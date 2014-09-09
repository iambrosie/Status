Mathematical Operators on Integers
==================================
In decreasing precence order: mod, *, /,  +, -.
These operators are left associative, e.g. a + b + c is equivalent to (a + b) + c rather than a + (b + c).
Also:

```
# min_int;;
- : int = -1073741824
```

and:

```
# max_int;;
- : int = 1073741823
```

Boolean Operators
=================
Only two boolean values, *true* and *false*.
Comparison operators: = (for equality testing), <, <=, >, >=, <>.
Two operators for combining boolean values: && (logical and) and || (local or). Note that *&& has a higher precedence than ||*, so a && b || c is the same as (a && b) || c.
Also, not is implemented as a function:

```
utop # not false;;
- : bool = true
```

Char
====
A char holds a single character and is written in single quotation marks.

```
# 'c';;
- : char = 'c'
```

If ... Then ... Else
====================

```
# if 100 > 99 then 0 else 1;;
- : int = 0
```

The expression between *if* and *else* must have type bool.
The types of the expression to choose if true and the expression to choose if false must be the same as one another (here they are both of type int).

Names
=====

```
utop # let x = 200 in x * x * x;;
- : int = 8000000
utop # let a = 500 in (let b = a * a in a + b);;
- : int = 250500
```

Functions
=========

```
utop # let cube x = x * x * x;;
val cube : int -> int = <fun>
utop # cube 200;;
- : int = 8000000 
```

cube is the name of the function and x is the name of its argument.

The cube function, as replied by OCaml is int -> int. That is, cube is a function which takes an integer as its argument and evaluates to an integer.

Of course, there can be more than one argument to a function, e.g.:

```
utop # let addtoten a b = a + b = 10;;
val addtoten : int -> int -> bool = <fun>
```

To indicate a recursive function, we use *let rec* instead of *let*, e.g.:

```
utop # let rec factorial a =
         if a = 1 then 1 else
           a * factorial (a - 1);;
val factorial : int -> int = <fun> 
```
