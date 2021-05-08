from parse import *
import math
import operator as op

# environment declaration

def standard_env():
    "An environment with some Scheme standard procedures."
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),  
		'print':   print,
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


#operands = ['+','-','*','/','>','<','>=', '<=','=']

class Env(dict):
    # basically is a dictionary of variable and its value in the outer env
    def __init__(self, parms = (), args = (), outer_env=None):
        self.update(zip(parms, args))
        self.outer_env = outer_env
    def find(self, variable):
        #searches for var
        return self if (variable in self) else self.outer_env.find(variable)


class Procedure(object):
    #user-defined procedure
    def __init__(self, parms, expression, env):
        self.parms = parms
        self.expression = expression
        self.env=env

    def __call__(self,*args):
        return eval(self.expression, Env(self.parms, args, self.env))

global_env = standard_env()   


def eval(x, env=global_env):
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):    # variable reference
        return env.find(x)[x]
    elif not isinstance(x, List):# constant 
        return x   
    op, *args = x       
    if op == 'quote':            # quotation
        return args[0]
    elif op == 'if':             # conditional
        (test, conseq, alt) = args
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif op == 'define':         # definition
        (symbol, exp) = args
        env[symbol] = eval(exp, env)
    elif op == 'set!':           # assignment
        (symbol, exp) = args
        env.find(symbol)[symbol] = eval(exp, env)
    elif op == 'lambda':         # procedure
        (parms, expression) = args
        return Procedure(parms, expression, env)
    else:                        # procedure call
        proc = eval(op, env)
        vals = [eval(arg, env) for arg in args]
        return proc(*vals)

        


def repl(prompt = 'lis-py> '):
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))

def schemestr(exp):
    if isinstance(exp,List):
        return '(' + ' '.join(map(schemestr,exp)) + ')'
    else:
        return str(exp)



