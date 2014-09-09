Mathematical Operators on Integers
==================================
In decreasing precence order: mod, *, /,  +, -.
These operators are left associative, e.g. a + b + c is equivalent to (a + b) + c rather than a + (b + c).
Also:
    '''
    # min_int;;
    - : int = -1073741824
    '''
and:
    '''
    # max_int;;
    - : int = 1073741823
    '''

Boolean Operators
=================
Only two boolean values, *true* and *false*.
Comparison operators: = (for equality testing), <, <=, >, >=, <>.
Two operators for combining boolean values: && (logical and) and || (local or). Note that *&& has a higher precedence than ||*, so a && b || c is the same as (a && b) || c.

Char
====
A char holds a single character and is written in single quotation marks.
    '''
    # 'c';;
    - : char = 'c'
    '''

If ... Then ... Else
====================
    '''
    # if 100 > 99 then 0 else 1;;
    - : int = 0
    '''
The expression between *if* and *else* must have type bool.
The types of the expression to choose if true and the expression to choose if false must be the same as one another (here they are both of type int).
