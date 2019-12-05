# Yacc example

import ply.yacc as yacc

from lexer import tokens


def p_process(p):
    '''
    process : create EXCLAMATION create EXCLAMATION join EXCLAMATION talk EXCLAMATION
    '''


def p_create(p):
    '''
    create : OPEN LB ID SEMICOLON NUMBER RB
    '''



def p_join(p):
    '''
    join : CONNECT LB RB
    '''

def p_talk(p):
    '''
    talk : SEND LB object RB
    '''

def p_object(p):
    '''
    object : ID
    '''
    print(p[1])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break

    parser.parse(s)