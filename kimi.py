# Kimi language interpreter in Python 3
# Anjana Vakil
# http://www.github.com/vakila/kimi

import sys

def tokenize(program):
    '''Take a Kimi program as a string, return the tokenized program as a list of strings.

    >>> tokenize("(+ 1 2)")
    ['(', '+', '1', '2', ')']

    >>> tokenize("(define square (lambda x (* x x)))")
    ['(', 'define', 'square', '(', 'lambda', 'x', '(', '*', 'x', 'x', ')', ')', ')']
    '''
    program = program.replace("(", " ( ")
    program = program.replace(")", " ) ")
    tokens = program.split()
    return tokens

def parse(tokens):
    pass

def evaluate(tree):
    pass


if __name__ == "__main__":
    program = sys.argv[1]
    print(tokenize(program))
