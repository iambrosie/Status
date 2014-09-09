OCaml Language Concepts
=======================

# General Notions

```
utop # 3.5 +. 6.;;
- : float = 9.5
utop # 300_000_000 / 300_000;;
- : int = 1000 
```

- We needed to type ;; in order to tell the toplevel that it should evaluate an expression. This is not required in standalone programs (but it is sometimes helpful to include ;; to improve OCaml’s error reporting, by making it more explicit where a given top-level declaration was intended to end).
- OCaml allows you to place underscores in the middle of numeric literals to improve readability. Note that underscores can be placed anywhere within a number, not just every three digits.
- OCaml distinguishes between *float*, the type for floating-point numbers, and *int*, the type for integers. The types have different literals (6. instead of 6) and different infix operators (+. instead of +), and OCaml doesn’t automatically cast between these types. This can be a bit of a nuisance, but it has its benefits, since it prevents some kinds of bugs that arise in other languages due to unexpected differences between the behavior of int and  float . For example, in many languages, 1/3 is zero, but 1/3.0 is a third. OCaml requires you to be explicit about which operation you’re doing.

# Variables

```
utop # let x = 3 + 4;;
val x : int = 7
utop # let y = x + x;;
val y : int = 14
```

- *let binding*: creating a variable to name the value of a given expression, using the *let* keyword.
- There are some constraints on what identifiers can be used for variable names. Punctuation is excluded, except for _ and  ', and variables must start with a lowercase letter or an underscore.
- By default, utop doesn’t bother to print out variables starting with an underscore.

# Functions

```
utop # let ratio x y = Float.of_int x /. Float.of_int y;;
val ratio : int -> int -> float = <fun>
utop # ratio 4 7;;
- : float = 0.571428571429
```

- Float.of_int refers to the of_int function contained in the Float module (contained in the Core.Std library). This is different from what you might expect from an object-oriented language, where dot-notation is typically used for accessing a method of an object.
- Module names always start with a capital letter.
- We can also write functions that take other functions as arguments:

```
utop # let sum_if_test test first second =
         (if test first then first else 0) +
           (if test second then second else 0);;
val sum_if_test : (int -> bool) -> int -> int -> int = <fun>

utop # let even x =
          x mod 2 = 0;;
val even : int -> bool = <fun>

utop # sum_if_test even 3 4;;
- : int = 4
```

- Even though we used = in two different ways: once as the part of the let binding that separates the thing  being defined from its definition; and once as an equality test, when comparing x mod 2 to 0. These are very different operations despite the fact that they share some syntax.

# Type Inference

