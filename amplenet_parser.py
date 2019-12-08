import ply.yacc as yacc

from file_reader import read_file
from amplenet_lexer import tokens
from server.server_controller import ServerController


controller = ServerController()


def p_process(p):
    '''
    process : create EXCLAMATION create EXCLAMATION join EXCLAMATION communication
            | join EXCLAMATION communication
    '''


def p_create_DEFAULT(p):
    '''
    create : DEFAULT LB ID RB
    '''
    controller.create_default(p[3])
    p[0]=p[3]


def p_create_IP(p):
    '''
    create : OPEN LB ID SEMICOLON IP SEMICOLON NUMBER RB
    '''
    controller.create_server(p[3], p[5], p[7])


def p_join(p):
    '''
    join : CONNECT LB ID SEMICOLON ID RB
        | CONNECT LB create SEMICOLON create RB
    '''
    controller.connect_server(p[3], p[5])


def p_communication(p):
    '''
    communication : talk EXCLAMATION communication
                | talk EXCLAMATION
    '''


def p_talk(p):
    '''
    talk : SEND LB ID SEMICOLON ID SEMICOLON MESSAGE RB
    '''
    controller.send_message(p[3], p[5], p[7])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input at '%s', at line %s character %s." % (p.value, p.lineno, p.lexpos))


# Build the parser
parser = yacc.yacc()


if __name__ == '__main__':
    s = read_file('tests/test2.txt')
    parser.parse(s)
