Linking and Loading
===================
The basic job of any **linker** or **loader** is simple: it *binds abstract names to concrete names*, which permits programmers to write code using the more abstract names, e.g. it takes a name written by a programmer, such as getline, and binds it to "the location 612 bytes from the beginning of the executable code in module iosys".

Actions performed by linkers and loaders:
  - *Program loading*.
  - *Relocation*.
  - *Symbol resolution*.