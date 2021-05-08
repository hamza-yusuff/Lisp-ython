# Scheme-ython

This project contains an implementation of a simple interpreter, and a transpiler written in python for Scheme and Racket respectively. The interpreter can deal with only a particular subset of Scheme, and supports user-defined procedures, variable handling, conditional (if), primitive data structures (except strings), and all sorts of mathematical operations. Currently, it does a very minimalistic error handling, and does not support a good number of primitive procedures, and for the time being, the transpiler only facilitates the following

- transpilation of mathematical infix operations written in Racket
- transpilation of cons to equivalent python list
- transpilation of lists in Racket to list in python
- variables which deal with the above operations

I used Peter Norvig's[http://norvig.com/lispy.html] implementation of the lisp interpreter as a general guideline for the interpreter. Special thanks to him.
For the transpiler, I architected algorithms, and deviced logic to initally parse the given racket code, and then produce the equivalent python code.

### Inspiration

I have built this project to essentially learn about interpreters, transpiler and the underlyings of the process involved. The reason for having a curiosity in this field comes from my inital struggle with functional progamming paradigm during my first term at University. As part of the introductory CS course, I had to learn Racket, and coming from an
imperitive programming background, it was bit difficult for me to pick up at first. That's when I started digging into transpiling and interpreters.  
Even though, this project is now fairly small, I plan to very soon integrate more functionality into the transpiler , and improve the existing interpretor.

- May 2021 - Currently, I am working on adding 'cond' transpilation into the transpiler and the error handling of the interpreter.

## Usage

The run.py contains a function called repl(), which upon invoking will initiate an interactive-read-eval-print loop. For the transpiler, you have to call the repl_translate()
function in translate.py to intitate a similar interactive-read-eval-print loop.

### Interpreter

### Transpiler

## Disclaimer

This project is built entirely from an educational standpoint. I wrote it mainly to know more about what goes under the hood during transpiling/interpreters/compiling languages, and get a first hand experience of writing one.

## Author

Hamza Yusuff - Email : hbyusuff@uwaterloo.ca
