OCaml Language Concepts
=======================

## General Notions

```
utop # 3.5 +. 6.;;
- : float = 9.5
utop # 300_000_000 / 300_000;;
- : int = 1000 
```

- We needed to type ;; in order to tell the toplevel that it should evaluate an expression. This is not required in standalone programs (but it is sometimes helpful to include ;; to improve OCaml’s error reporting, by making it more explicit where a given top-level declaration was intended to end).
- OCaml allows you to place underscores in the middle of numeric literals to improve readability. Note that underscores can be placed anywhere within a number, not just every three digits.
- OCaml distinguishes between *float*, the type for floating-point numbers, and *int*, the type for integers. The types have different literals (6. instead of 6) and different infix operators (+. instead of +), and OCaml doesn’t automatically cast between these types. This can be a bit of a nuisance, but it has its benefits, since it prevents some kinds of bugs that arise in other languages due to unexpected differences between the behavior of int and  float . For example, in many languages, 1/3 is zero, but 1/3.0 is a third. OCaml requires you to be explicit about which operation you’re doing.

## Variables

```
utop # let x = 3 + 4;;
val x : int = 7
utop # let y = x + x;;
val y : int = 14
```

- *let binding*: creating a variable to name the value of a given expression, using the *let* keyword.
- There are some constraints on what identifiers can be used for variable names. Punctuation is excluded, except for _ and  ', and variables must start with a lowercase letter or an underscore.
- By default, utop doesn’t bother to print out variables starting with an underscore.

## Functions

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

- Even though we used = in two different ways (in the even function): once as the part of the let binding that separates the thing  being defined from its definition; and once as an equality test, when comparing x mod 2 to 0. These are very different operations despite the fact that they share some syntax.

## Type Inference

- OCaml determines the type of an expression using a technique called *type inference*, by which the type of an expression is inferred from the available type information about the components of that expression.
- You can make it easier to understand the types of a given expression by adding explicit type annotations:

```
utop # let sum_if_test (test : int -> bool) (first : int) (second : int) : int =
         (if test first then first else 0) +
           (if test second then second else 0);;
val sum_if_test : (int -> bool) -> int -> int -> int = <fun> 
```

- These annotations don’t change the behavior of an OCaml program, but they can serve as useful documentation, as well as catch unintended type changes. They can also be helpful in figuring out why a given piece of code fails to compile.
- The final annotation indicates the type of the return value (for the sum_if_test function).

## Infering Generic Types

```
utop # let first_if_true test x y =
         if test x then x else y;;
val first_if_true : ('a -> bool) -> 'a -> 'a -> 'a = <fun>
```

- So what’s the type of first_if_true ?
  - Since there are no obvious clues such as arithmetic operators or literals to tell you what the type of x and y are, that makes it seem like one could use first_if_true on values of any type.
  - By looking at the type returned by the toplevel, we can see that rather than choose a single concrete type, OCaml has introduced a type variable, 'a, to express that the type is generic.
  - test is a one-argument function whose return value is bool and whose argument could be of any type 'a. But, whatever type 'a is, it has to be the same as the type of the other two arguments, x and y, and of the return value of first_if_true.
- This kind of genericity is called *parametric polymorphism* because it works by parameterizing the type in question with a type variable.
- The generic type of first_if_true allows us to write something like this:

```
utop # let long_string s = String.length s > 6;;
val long_string : string -> bool = <fun>

utop # first_if_true long_string "short" "loooooooooooooong";;
- : string = "loooooooooooooong"
```

- But we can just as well write something like this:

```
utop # let big_number x = x > 3;;
val big_number : int -> bool = <fun>

utop # first_if_true big_number 10 20;;
- : int = 10
```

## Type Errors Versus Exceptions

- The distinction between *type errors* and *exceptions* is that type errors will stop you whether or not the offending code is ever actually executed, whereas code that triggers exceptions only fails when it’s called, and then, only when it’s called with an input that triggers the exception.