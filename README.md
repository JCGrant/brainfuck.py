# brainfuck.py

An interpreter for the [Brainfuck language](http://www.muppetlabs.com/~breadbox/bf/), written in Python.

## Usage
Pass a brainfuck program into it as an argument:

    ./brainfuck.py [file]

It can read from stdin:

    echo [brainfuck-string] | ./brainfuck

Or you can use it as a module:

    from brainfuck import BrainfuckInterpreter
    bfi = BrainfuckInterpreter()
    bfi.run(program)
