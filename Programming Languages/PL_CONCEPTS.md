Computability
=============
From a mathematical point of view, *a program defines a function*. The *output* of a program is computed as a function of the program inputs and the state of the machine before the program starts.

In computation, there are two different reasons why an expression might not have a value:
1. *Error termination* (e.g. Division by zero)
2. *Nontermination* (i.e. There is a specific computation to perform, but the computation may not terminate and therefore may not yield a value.)

A *partial function* is a function that is defined on some arguments and undefined on others. 

Programs actually define partial functions.

The class of functions on the natural numbers that are computable in principle (and not computable in practice, because some computable functions may take an extremely long time to finish) is often called the class of *partial recursive functions*.

A function f : A -> B is *computable* if there is an algorithm that, given any x in A as input, halts with y = f(x) as output. That is, *a function is computable if there is some program that computes it*.

*Church’s thesis*: the same class of functions on the integers can be computed by any general computing device. The fact that all standard programming languages express precisely the class of partial recursive functions is often summarized by the statement that *all programming languages are Turing complete*.

Some specific functions are *not computable*, e.g. *the halting problem*:
  - The halting problem is stated for programs that require one string input. If P is such a program and x is a string input, then we write P(x) for the output of program P on input x.
  - Given a program P that requires exactly one string input and a string x, determine whether P halts on input x.

The undecidability of the halting problem implies that some properties of programs cannot be determined in advance, e.g. it is not possible for a compiler to determine whether certain loops will halt.

Summary: When the value of a function or the value of an expression is undefined because a basic operation such as division by zero does not make sense,a compiler or interpreter can cause the program to halt and report the error. However, the undecidability of the halting problem implies that there is no way to detect and report an error whenever a program is not going to halt.

For more computability and complexity theory:
  - Introduction to Automata Theory, Languages, and Computation by Hopcroft, Motwani, and Ullman
  - Introduction to the Theory of Computation by Sipser