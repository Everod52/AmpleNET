# Yacc example

import ply.yacc as yacc

from lexer import tokens
from server.server_controller import ServerController

controller = ServerController()


def p_process(p):
    '''
    process : create EXCLAMATION create EXCLAMATION join EXCLAMATION talk EXCLAMATION
    '''


def p_create(p):
    '''
    create : OPEN LB ID SEMICOLON ID SEMICOLON NUMBER RB
    '''
    controller.create_server(p[3], p[5], p[7])


def p_join(p):
    '''
    join : CONNECT LB ID SEMICOLON ID RB
    '''
    controller.connect_server(p[3],p[5])


def p_talk(p):
    '''
    talk : SEND LB ID SEMICOLON ID SEMICOLON object RB
    '''
    controller.send_message(p[3],p[5],p[7])


def p_object(p):
    '''
    object : ID
    '''
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input at %s" %p )


# Build the parser

parser = yacc.yacc()

# if __name__ == '__main__':
#     while True:
#         try:
#             s = input('')
#         except EOFError:
#             break
#
#         parser.parse(s)
