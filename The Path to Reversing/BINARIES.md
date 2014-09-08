[how to read an executable] (http://jvns.ca/blog/2014/09/06/how-to-read-an-executable/)
=======================================================================================

terms
=====
* **symbols** - used to answer the question “if i call a function and it’s defined somewhere else, how do i find it?”
* symbols are organized into **sections** - code lives in one section (.text) and data in another (.data, .rodata)
* sections are organized into **segments**

tools
=====
* readelf
* nm
* objdump

elf file structure
==================
* [elf 101] (https://code.google.com/p/corkami/wiki/ELF101)

linkers
=======
* [20 part linker essay] (http://lwn.net/Articles/276782/)