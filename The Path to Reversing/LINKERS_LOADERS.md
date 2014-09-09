Linking and Loading
===================
The basic job of any **linker** or **loader** is *binding abstract names to concrete names*. This permits programmers to write code using more abstract names, e.g. taking a name written by a programmer, such as getline, it binds it to "the location 612 bytes from the beginning of the executable code in module iosys".

Actions performed by linkers and loaders:
  - *Program loading*
  - *Relocation*
  - *Symbol resolution*