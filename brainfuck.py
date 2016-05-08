#!/usr/bin/env python3

import sys

class Tape(object):
    
    def __init__(self):
        self._tape = [0]
        self.pointer = 0

    def get(self):
        return self._tape[self.pointer]

    def set(self, value):
        self._tape[self.pointer] = value

    def shift_right(self):
        self.pointer += 1
        if self.pointer == len(self._tape):
            self._tape.append(0)

    def shift_left(self):
        self.pointer -= 1

    def increment(self):
        self._tape[self.pointer] += 1

    def decrement(self):
        self._tape[self.pointer] -= 1

    def is_zero(self):
        return self.get() == 0

    def is_not_zero(self):
        return not self.is_zero()



class BrainfuckInterpreter(object):
    
    allowed_chars = '><+-.,[]'

    def __init__(self):
        self.program_counter = 0
        self.tape = Tape()

    def write(self):
        sys.stdout.write(chr(self.tape.get()))

    def read(self):
        self.tape.set(ord(sys.stdin.read(1)))

    def jump_to_matching_bracket(self):
        self.program_counter = self.bracket_map[self.program_counter]

    def open_bracket(self):
        if self.tape.is_zero():
            self.jump_to_matching_bracket()

    def close_bracket(self):
        if self.tape.is_not_zero():
            self.jump_to_matching_bracket()

    def interpret_instruction(self):
        current_instruction = self.program[self.program_counter]
        {
            '>': self.tape.shift_right,
            '<': self.tape.shift_left,
            '+': self.tape.increment,
            '-': self.tape.decrement,
            '.': self.write,
            ',': self.read,
            '[': self.open_bracket,
            ']': self.close_bracket
        }[current_instruction]()

    def parse(self, program):
        bracket_stack = []
        bracket_map = {}
        parsed_program = ''
        program_counter = 0
        for character in program:
            if character in self.allowed_chars:
                parsed_program += character
                if character == '[':
                    bracket_stack.append(program_counter)
                if character == ']':
                    left_bracket_position = bracket_stack.pop()
                    right_bracket_position = program_counter
                    bracket_map[left_bracket_position] = right_bracket_position
                    bracket_map[right_bracket_position] = left_bracket_position
                program_counter += 1
        return parsed_program, bracket_map

    def interpret(self, program):
        self.program, self.bracket_map = self.parse(program)
        while self.program_counter < len(self.program):
            self.interpret_instruction()
            self.program_counter += 1


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        f = open(filename, "r")
    else:
        print("Usage: {} [file]".format(__file__))
        sys.exit(1)
    program = f.read()
    bfi = BrainfuckInterpreter()
    bfi.interpret(program)

if __name__ == '__main__':
    main()
