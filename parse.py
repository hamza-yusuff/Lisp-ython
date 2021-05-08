import math
import operator as op


program = "(begin (define r 10) (* pi (* r r)))"

Symbol = str              #  Lisp Symbol is implemented as a Python str
Number = (int, float)     #  Lisp Number is implemented as a Python int or float
Atom   = (Symbol, Number) #  Lisp  Atom is a Symbol or Number
List   = list             #  Lisp List is implemented as a Python list
Exp    = (Atom, List)     #  Lisp expression is an Atom or List
Env    = dict             #  Lisp environment which is essentially a dictionary
                          # of {'var':'value'}

def tokenize(chars):
    return chars.replace('(',' ( ').replace(')',' ) ').split()


def parse(chars):
    return read_from_tokens(tokenize(chars))


def read_from_tokens(parsed):
    if len(parsed)==0:
        raise SyntaxError('invalid syntax')
    parse =parsed.pop(0)
    if parse =='(':
        l=[]
        while parsed[0] != ')':
            l.append(read_from_tokens(parsed))
        parsed.pop(0)
        return l
    elif parse ==')':
        raise SyntaxError('unexpected )')
    else:
        return atom(parse)

def atom(string):
    try:
        return int(string)
    except ValueError:
        try :
            return float(string)
        except ValueError:
            return Symbol(string)