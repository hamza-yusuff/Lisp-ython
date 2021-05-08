from transpile import *
from run import *

operands = ['+','-','*','/','>','<','>=', '<=','=']
# translate
def translate(expression, env=global_env):
    x = parse(expression)
    if x[0] == 'define':
        (_, symbol, exp) = x

        if  exp[0] == 'list':
            print(symbol+' = ', end='')
            print(concat_list(exp[1:]))

        elif exp[0] == 'cons':
            print(symbol+' = ', end=' ')
            print(concat_cons(find_cons(expression[1:]))) # parses the orginal expression
        else:
            print(symbol+' = '+ concat(exp))
        
    elif str(x[0]) in operands:
        print(concat(x))
    elif str(x[0])=='list':
        print(concat_list(x[1:]))
    elif str(x[0]) == 'cons':
        print(concat_cons(expression))
    

def repl_translate(prompt = 'translate-code : > '):
    while True:
        val = translate(input(prompt))
