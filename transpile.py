from parse import *
from run import *

operands = ['+','-','*','/','>','<','>=', '<=','=']

def concat(exp) :
    s=''
    i=0
    while i<len(exp):
        k = i
        #print(exp[i])
        if not isinstance(exp[i],list):
            
            if str(exp[i]) in operands: # if there is list of operation within
                if not isinstance(exp[i+1],list):
                    s+=str(exp[i+1])
                else:
                    s+='('+concat(exp[i+1])+')'
                s+=str(exp[i])
                i+=2
            else:
                s+=str(exp[i])
        else :
            s+='('+concat(exp[i])+')'
        if (k==i):
            i+=1
        
    return s

def concat_list(exp):
    arr=[]
    for k in exp:
        if isinstance(k, list):
            arr.append(concat_list(k[1:]))
        else:
            arr.append(k)
    return arr


def concat_cons(exp):
    arr = exp.replace('(cons', ' ').replace('empty', ')').replace(')', ' ').split(' ')
    new = []
    for element in arr:
        if element!='':
            new.append(element)
    return new



def find_cons(exp):
    find = 0
    length = len(exp)
    for i in range(length):
        if exp[i] == '(':
            find = i
            break

    if find == 0:
        raise Exception("String not supported")
    else:
        return exp[i:length-1]
