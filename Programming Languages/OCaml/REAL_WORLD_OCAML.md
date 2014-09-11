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

## Tuples

- A tuple is an ordered collection of values that can each be of a different type.

```
utop # let a_tuple = (3, "four", 5.);;
val a_tuple : int * string * float = (3, "four", 5.)
```

- You can extract the components of a tuple using pattern matching, as shown below (here, the (x, y) is the pattern):

```
utop # let (x, y, z) = a_tuple;;
val x : int = 3                                                                     val y : string = "four"                                                             val z : float = 5.
```

- Pattern matching can also show up in function arguments. If we represent a point on the plane as a pair of floats, we can use the following function to compute their distance:

```
utop # let distance (x1, y1) (x2, y2) =
         sqrt((x1 -. x2) ** 2. +. (y1 -. y2) ** 2. );;
val distance : float * float -> float * float -> float = <fun>
```

## Lists

- Where tuples let you combine a fixed number of items, potentially of different types, *lists let you hold any number of items of the same type*.

```
utop # let alist = ["string1"; "string2"; "string3"];;
val alist : string list = ["string1"; "string2"; "string3"]
```

- OCaml uses semicolons to separate list elements in lists rather than commas. Commas, instead, are used for separating elements in a tuple.

- In addition to constructing lists using brackets, we can use the operator :: for adding elements to the front of a list (this creates a new and extended list and does not change the list we started with):

```
utop # "string-1" :: "string0" :: alist;;
- : string list = ["string-1"; "string0"; "string1"; "string2"; "string3"]
```

- The bracket notation for lists is really just syntactic sugar for ::. Thus, the following declarations are all equivalent. Note that [] is used to represent the empty list and that :: is right-associative:

```
utop # [1; 2; 3];;
- : int list = [1; 2; 3]
utop # 1 :: (2 :: (3 :: []));;
- : int list = [1; 2; 3]
utop # 1 :: 2 :: 3 :: [];;
- : int list = [1; 2; 3]
```

- There’s also a list concatenation operator, @, which can concatenate two lists (however, unlike  ::, this is not a constant-time operation. Concatenating two lists takes time proportional to the length of the first list):

```
utop # [1; 2; 3] @ [4; 5; 6];;
- : int list = [1; 2; 3; 4; 5; 6]
```

- The elements of a list can be accessed through pattern matching. List patterns are based on the two list constructors, [] and ::

```
utop # let my_string alist =
         match alist with
           | first :: the_rest -> first
           | [] -> "whatever" (* the default*)
       ;;

utop # my_string ["la"; "ala"; "alal"];;
- : string = "la"

utop # my_string [];;
- : string = "whatever"
```

- The first pattern, first :: the_rest, covers the case where alist has at least one
element, since every list except for the empty list can be written down with one or
more :: ’s. The second pattern, [], matches only the empty list. These cases are exhaustive, since every list is either empty or has at least one element, a fact that is verified by the compiler.

- Recursive list functions:

```
utop # let rec sum l = 
         match l with
           | [] -> 0                  (* the base case, l is an empty list *)
           | hd :: tl -> hd + sum tl  (* the inductive case, where l is a non-empty list *)
       ;;
val sum : int list -> int = <fun>

utop # sum [1; 2; 3];;
- : int = 6
```

## Option

- An option is used to express that a value might or might not be present. For example:

```
utop # let divide x y =
         match y with
           | 0 -> None
           | _ -> Some (x / y)
       ;;
val divide : int -> int -> int option = <fun>

utop # divide 3 0;;
- : int option = None

utop # divide 3 2;;
- : int option = Some 1
```

- Some and None are constructors that let you build optional values, just as :: and [] let you build lists. You can think of an option as a specialized list that can only have zero or one elements.

- To examine the contents of an option, we use pattern matching, as we did with tuples and lists.

```
utop # let log_entry maybe_time message =
         let time =
           match maybe_time with
             | Some x -> x
             | None -> Time.now ()                    (* Core’s Time module *)
         in
           Time.to_sec_string time ^ " -- " ^ message (* ^ is the string concatenation operator *)
       ;;
val log_entry : Time.t option -> string -> string = <fun>

utop # log_entry None "bla";;
- : string = "2014-09-11 16:14:29 -- bla"

utop # log_entry (Some Time.epoch)  "bla";;
- : string = "1970-01-01 02:00:00 -- bla"
```

- Options are important because they are the standard way in OCaml to encode a value
that might not be there; there’s no such thing as a NullPointerException in OCaml (this is in contrast with most other languages, including Java and C#, where most if not all data types are nullable, meaning that, whatever their type is, any given value also contains the possibility of being a null value. In such languages, null is lurking everywhere).

## Records and Variants

- OCaml also allows us to define new data types. Here’s a toy example of a data type representing a point in two-dimensional space:

```
utop # type point2d = { x : float; y : float };;
type point2d = { x : float; y : float; }

utop # let p = { x = 3.; y = -4. };;
val p : point2d = {x = 3.; y = -4.}
```

- point2d is a *record* type, which you can think of as a tuple where the individual fields are named, rather than being defined positionally.

- We can get access to the contents of these types using pattern matching:

```
utop # let magnitude { x = x_pos ; y = y_pos } =
         sqrt (x_pos ** 2. +. y_pos ** 2.);;
val magnitude : point2d -> float = <fun>
```

- This can be written more tersely using what’s called *field punning* (when the
name of the field and the name of the variable it is bound to coincide, we don’t have to write them both down):

```
utop # let magnitude { x; y } = sqrt (x ** 2. +. y ** 2.);;
val magnitude : point2d -> float = <fun>
```

- Alternatively, we can use dot notation for accessing record fields:

```
utop # let distance v1 v2 =
         magnitude { x = v1.x -. v2.x; y = v1.y -. v2.y }
       ;;
val distance : point2d -> point2d -> float = <fun>
```

## Imperative Programming